from .SeedTransducerManager import SeedTransducerManager
from .CodeGenerator import CodeGenerator
from .DecorationTableManager import DecorationTableManager
from .APFAutomatonGenerator import APFAutomatonGenerator

def gen(path):

    # instanciating seed transducers for every registered patterns
    seed_transducers = SeedTransducerManager('../input/seed.pl')
    
    # instanciating decoration tables
    decoration_tables = DecorationTableManager('../input/tables.pl')
    
    c = CodeGenerator()
    c.begin(tab="    ")
    
    # generating pattern recognition function for every patterns
    APFAutomatonGenerator.genAll(c, decoration_tables, seed_transducers)
        
    output_file = open(path, "w")
    output_file.write(c.end())
    output_file.close()