from . import aggregators_code_generator, features_code_generator


class APFAutomatonGenerator:

    aggregators = ['max', 'min', 'sum']
    features = ['one', 'width', 'surface', 'max', 'min', 'range']

    @staticmethod
    def genAll(code_generator, decoration_table, seed_transducer):
        for aggregator in aggregators:
            for feature in features:
                gen(code_generator, decoration_table, seed_transducer, aggregator, feature)

    @staticmethod
    def gen(code_generator, decoration_table, seed_transducer, aggregator, feature):
        c = code_generator
        dt = decoration_table
        st = seed_transducer
        a = APFAutomatonGenerator.getAggregatorGenerator(aggregator)
        f = APFAutomatonGenerator.getFeatureGenerator(feature)

        c.writeln("def " + aggregator + "_" + feature + "_" + st.pattern + "(sequence):")
        c.indent()
        c.writeln("n = len(sequence)") # Needed for features attribute code generator
        c.writeln("signature_sequence = list()")
        c.writeln("t_occurences = list()")

        c.writeln("aggregate = list()")
        c.writeln("current = list()")
        c.writeln("potential = list()")

        # Initializing accumulators
        c.writeln("R = " + a.default(f))
        c.writeln("C = " + a.default(f))
        c.writeln("D = " + f.neutral())
        
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
        c.writeln("signature_sequence.append(symbol)")
        first_if = True
        for state in st.states:
            state_name = state.name
            c.writeln(("el" if first_if == False else "") + ("if 'current_state' not in locals() or " if state.is_entry_state else "if ") + " current_state == '" + state_name + "':")
            first_if = False
            c.indent()
            for transition in state.transitions:
                c.writeln("if symbol == '" + transition.input + "':")
                c.indent()
                c.writeln("t_occurences.append('" + transition.output+ "')")

                # Updating accumulators
                APFAutomatonGenerator.genAccumulatorUpdate(c, dt, a, f, "R", transition.output)
                APFAutomatonGenerator.genAccumulatorUpdate(c, dt, a, f, "C", transition.output)
                APFAutomatonGenerator.genAccumulatorUpdate(c, dt, a, f, "D", transition.output)

                c.writeln("current_state = '" + transition.next + "'")  
                c.dedent()
            c.dedent()
        c.dedent()
        c.writeln("previous_number = number")
        c.writeln("aggregate.append(R)")
        c.writeln("current.append(C)")
        c.writeln("potential.append(D)")
        c.dedent()
        c.writeln("print(aggregate)")
        c.writeln("print(current)")
        c.writeln("print(potential)")
        c.writeln("return " + a.aggregate("R", "C"))
        c.dedent()

    @staticmethod
    def genAccumulatorUpdate(code_generator, decoration_table, aggregator, feature, accumulator, semantic_letter):
        if(decoration_table.hasUpdate(accumulator, semantic_letter)):
            operation = decoration_table.getUpdate(accumulator, semantic_letter)
            operation = operation.replace(")", "")
            code_generator.writeln(accumulator + " = " + APFAutomatonGenerator.convertOperation(aggregator, feature, operation))

    @staticmethod
    def convertOperation(aggregator, feature, operation):
        splittedOp = operation.split("(", 1)
        func = splittedOp[0]
        if(len(splittedOp) > 1):
            arg1, arg2 = splittedOp[1].split(",", 1)   
            arg1 = APFAutomatonGenerator.convertOperation(aggregator, feature, arg1)
            arg2 = APFAutomatonGenerator.convertOperation(aggregator, feature, arg2)

        if(func == "neutral"):
            return feature.neutral()
        elif(func == "min"):
            return feature.min()
        elif(func == "max"):
            return feature.max()
        elif(func == "phi"):
            return feature.phi(arg1, arg2)
        elif(func == "delta"):
            return feature.delta()
        elif(func == "default"):
            return aggregator.default(feature)
        elif(func == "a"):
            return aggregator.aggregate(arg1, arg2)
        elif(func in {"C", "R", "D"}):
            return func
        else:
            raise ValueError("Function " + func + " doesn't exist.")

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

    