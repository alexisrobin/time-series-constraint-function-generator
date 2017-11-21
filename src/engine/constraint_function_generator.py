from .SeedTransducer import SeedTransducer
from .CodeGenerator import CodeGenerator
from .DecorationTableManager import DecorationTableManager
from .APFAutomatonGenerator import APFAutomatonGenerator

def gen(path):

    # instanciating seed transducers for every registered patterns
    seed_transducers = list()
    lines = [line.rstrip('\n') for line in open('../input/seed_transducers.data')]
    for line in lines:
        seed_transducers.append(SeedTransducer(line))
    
    # instanciating decoration tables
    decoration_table = DecorationTableManager('../input/tables.pl')
    
    # generating pattern recognition function for every patterns
    c = CodeGenerator()
    c.begin(tab="    ")
    for st in seed_transducers:
        APFAutomatonGenerator.genAll(c, decoration_table, st)
        
    output_file = open(path, "w")
    output_file.write(c.end())
    output_file.close()