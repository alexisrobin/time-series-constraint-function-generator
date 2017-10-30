from .automata import Automata

class SeedTransducer:

    input_alphabet =  ['<','=','>']
    output_alphabet = ['out','outr','outa','maybeb','maybea','founde','found','in']

    def __init__(self, line):
        self.automata = Automata(self.input_alphabet, self.output_alphabet)
        details, states = line.split("?")
        self.pattern, self.b, self.a = details.split(";")
        #for state in states.split(";"):

        


