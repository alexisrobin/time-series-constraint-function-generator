from .SeedTransducer import SeedTransducer
from .CodeGenerator import CodeGenerator
from .DecorationTable import DecorationTable
from .APFAutomatonGenerator import APFAutomatonGenerator

def gen(path):

    # instanciating seed transducers for every registered patterns
    seed_transducers = list()
    lines = [line.rstrip('\n') for line in open('../input/seed_transducers.data')]
    for line in lines:
        seed_transducers.append(SeedTransducer(line))
    
    # instanciating decoration table
    decoration_table = DecorationTable('../input/decoration_tables.data')
    
    # generating pattern recognition function for every patterns
    c = CodeGenerator()
    c.begin(tab="    ")
    for st in seed_transducers:
        APFAutomatonGenerator.gen(c, decoration_table, st, 'min', 'width')
        APFAutomatonGenerator.gen(c, decoration_table, st, 'min', 'surface')
        APFAutomatonGenerator.gen(c, decoration_table, st, 'min', 'max')
        APFAutomatonGenerator.gen(c, decoration_table, st, 'min', 'min')
        
    output_file = open(path, "w")
    output_file.write(c.end())
    output_file.close()