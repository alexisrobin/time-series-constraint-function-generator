from .SeedTransducer import SeedTransducer
from .CodeGenerator import CodeGenerator

def gen(path):

    # instanciating seed transducers for every registered patterns
    seed_transducers = list()
    lines = [line.rstrip('\n') for line in open('../input/seed_transducers.data')]
    for line in lines:
        seed_transducers.append(SeedTransducer(line))
    
    # generating pattern recognition function for every patterns
    c = CodeGenerator()
    c.begin(tab="    ")
    for st in seed_transducers:
        c.writeln("def " + st.pattern + "(signature_sequence):")
        c.indent()
        c.writeln("n = len(signature_sequence)") # Needed for features attribute code generator
        c.writeln("t_occurences = list()")
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
    output_file = open(path, "w")
    output_file.write(c.end())
    output_file.close()