class State:

    def __init__(self, name):
        self.name = name
        self.transitions = {}

    def addTransition(self, input, output):
        self.transitions[input] = output

    def output(self, input):
        return self.transitions[input]

class Automata:

    def __init__(self, input_alphabet, output_alphabet):
        self.input_alphabet = input_alphabet
        self.output_alphabet = output_alphabet