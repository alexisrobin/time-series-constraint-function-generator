class State:

    def __init__(self, name):
        self.name = name
        self.transitions = {}

    def addTransition(self, input, output):
        self.transitions[input] = output

    def output(self, input):
        return self.transitions[input]

class SeedTransducer:

    input_alphabet =  ['<','=','>']
    output_alphabet = ['out','outr','outa','maybeb','maybea','founde','found','in']

    def __init__(self, line):
        self.states = {}
        details, states = line.split("?")
        self.pattern, self.b, self.a = details.split(";")
        for state in states.split(";"):
            name, *transitions = state.split(",")
            self.addState(name)
            for transition in transitions:
                inputs, output = transition.split(':')
                for input in inputs:
                    self.getState(name).addTransition(input, output)
        self.print()

    def addState(self, name):
        self.states[name] = State(name)

    def getState(self, name):
        return self.states[name]

    def print(self):
        print("[" + self.pattern + "]")
        for x in self.states:
            state = self.states[x]
            print("(" + state.name + ") => ")
            for input in state.transitions:
                print(input + ":" + state.transitions[input])
    
    def run(self, signature_sequence):
        print("run")
