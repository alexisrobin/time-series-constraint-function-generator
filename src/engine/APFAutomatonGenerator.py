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

        c.writeln("def " + aggregator + "_" + feature + "_" + st.pattern + "(signature_sequence):")
        c.indent()
        c.writeln("n = len(signature_sequence)") # Needed for features attribute code generator
        c.writeln("t_occurences = list()")

        # Accumulators initialisation
        c.writeln("R = " + a.default(f))
        c.writeln("C = " + a.default(f))
        c.writeln("D = " + f.neutral())
        
        c.writeln("for symbol in signature_sequence:")
        c.indent()
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
                c.writeln("current_state = '" + transition.next + "'")  
                c.dedent()
            c.dedent()
        c.dedent()
        c.writeln("return t_occurences")
        c.dedent()

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

    