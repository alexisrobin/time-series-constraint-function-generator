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
        c.writeln("for symbol in signature_sequence:")
        c.indent()
        c.writeln("print(symbol)")
    output_file = open(path, "w")
    output_file.write(c.end())
    output_file.close()