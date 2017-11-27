from . import aggregators_code_generator, features_code_generator, util

class APFAutomatonGenerator:

    aggregators = ['max', 'min', 'sum']
    features = ['one', 'width', 'surface', 'max', 'min', 'range']

    @staticmethod
    def genAll(code_generator, dt_manager, st_manager):
        for aggregator in APFAutomatonGenerator.aggregators:
            for feature in APFAutomatonGenerator.features:
                for pattern in st_manager.seed_transducers:
                    APFAutomatonGenerator.gen(code_generator, dt_manager, st_manager.seed_transducers[pattern], aggregator, feature)

    @staticmethod
    def gen(code_generator, dt_manager, seed_transducer, aggregator, feature):
        c = code_generator
        st = seed_transducer
        a = APFAutomatonGenerator.getAggregatorGenerator(aggregator)
        f = APFAutomatonGenerator.getFeatureGenerator(feature)
        table_name = APFAutomatonGenerator.getDecorationTableNameForFeature(feature)
        accumulators = dt_manager.getAccumulatorsLetter(table_name)

        c.writeln("def " + aggregator + "_" + feature + "_" + st.pattern + "(sequence):")
        c.indent()
        c.writeln("n = len(sequence)") # Needed for features attribute code generator
        #c.writeln("signature_sequence = list()")
        #c.writeln("t_occurences = list()")

        # Initializing accumulators
        for accumulator in accumulators:
            c.writeln(accumulator + "=" + APFAutomatonGenerator.getUpdate(dt_manager, table_name, a, f, dt_manager.INIT, dt_manager.NO_AFTER, accumulator))
        
        c.writeln("for i, number in enumerate(sequence):")
        c.indent()
        c.writeln("if 'previous_number' in locals():")
        c.indent()
        c.writeln("if previous_number > number:")
        c.indent()
        c.writeln("symbol = '>'")
        c.dedent()
        c.writeln("elif previous_number < number:")
        c.indent()
        c.writeln("symbol = '<'")
        c.dedent()
        c.writeln("else:")
        c.indent()
        c.writeln("symbol = '='")
        c.dedent()
        #c.writeln("signature_sequence.append(symbol)")
        c.writeln("delta = " + f.delta())
        c.writeln("deltaprime = " + f.deltaprime())
        first_if = True
        for letter, state in st.states.items():
            state_name = state.name
            c.writeln(("el" if first_if == False else "") + ("if 'current_state' not in locals() or " if state.is_entry_state else "if ") + " current_state == '" + state_name + "':")
            first_if = False
            c.indent()
            for transition in state.transitions:
                c.writeln("if symbol == '" + transition.input + "':")
                c.indent()
                #c.writeln("t_occurences.append('" + transition.output+ "')")

                # Updating accumulators in tmp variable because accumulators updates are simultaneous
                for accumulator in accumulators:
                    c.writeln(accumulator + "_tmp = " + APFAutomatonGenerator.getUpdate(dt_manager, table_name, a, f, transition.output, st.after, accumulator))
                for accumulator in accumulators:
                    c.writeln(accumulator + " = " + accumulator + "_tmp")

                c.writeln("current_state = '" + transition.next + "'")  
                c.dedent()
            c.dedent()
        c.dedent()
        c.writeln("previous_number = number")
        c.dedent()
        c.writeln("return " + APFAutomatonGenerator.getFinal(dt_manager, table_name, a, f))
        c.dedent()
        c.writeln("")

    @staticmethod
    def getFinal(dt_manager, table_name, aggregator, feature):
        operation = dt_manager.getFinal(table_name)
        return APFAutomatonGenerator.genUpdate(aggregator, feature, operation)

    @staticmethod
    def getUpdate(dt_manager, table_name, aggregator, feature, semantic_letter, after, accumulator):
        operation = dt_manager.getUpdate(table_name, semantic_letter, after, accumulator)
        return APFAutomatonGenerator.genUpdate(aggregator, feature, operation)

    @staticmethod
    def genUpdate(aggregator, feature, operation):
        splittedOp = operation.split("(", 1)
        func = splittedOp[0]
        if(len(splittedOp) > 1):
            args = util.top_level_split(splittedOp[1])
            args = [ APFAutomatonGenerator.genUpdate(aggregator, feature, x) for x in args ]
            
        func = func.replace(")", "")
        if(func == "neutral"):
            return feature.neutral()
        elif(func == "min"):
            return feature.min()
        elif(func == "max"):
            return feature.max()
        elif(func == "f"):
            return feature.phi(args[0], args[1])
        elif(func == "default"):
            return aggregator.default(feature)
        elif(func == "g"):
            return aggregator.aggregate(args[0], args[1])
        elif(func == "first"):
            return "sequence[0]"
        else:
            ret = func
            if('args' in locals()):
                ret += "("
                for i, arg in enumerate(args):
                    ret += arg
                    if(len(args) > i+1):
                        ret += ","
                ret += ")"
            return ret

    @staticmethod
    def getAggregatorGenerator(aggregator):
        if(aggregator == "max"):
            return aggregators_code_generator.Max()
        elif(aggregator == "min"):
            return aggregators_code_generator.Min()
        elif(aggregator == "sum"):
            return aggregators_code_generator.Sum()
        else:
            raise ValueError("Aggregator " + aggregator + "doesn't exist.")

    @staticmethod
    def getFeatureGenerator(feature):
        if(feature == "one"):
            return features_code_generator.One()
        elif(feature == "width"):
            return features_code_generator.Width()
        elif(feature == "surface"):
            return features_code_generator.Surface()
        elif(feature == "max"):
            return features_code_generator.Max()
        elif(feature == "min"):
            return features_code_generator.Min()
        elif(feature == "range"):
            return features_code_generator.Range()
        else:
            raise ValueError("Feature " + feature + "doesn't exist.")
    
    @staticmethod
    def getDecorationTableNameForFeature(feature):
        if(feature == "range"):
            return "range_function"
        else:
            return "function"

    