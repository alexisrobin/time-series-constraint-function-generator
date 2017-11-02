class Transition:

    def __init__(self, input, output, next):
        self.input = input
        self.output = output
        self.next = next

class State:

    def __init__(self, name, is_entry_state = False):
        self.name = name
        self.transitions = list()
        self.is_entry_state = is_entry_state

    def addTransition(self, input, output, next):
        self.transitions.append(Transition(input, output, next))

class SeedTransducer:

    input_alphabet =  ['<','=','>']
    output_alphabet = ['out','outr','outa','maybeb','maybea','founde','found','in']

    def __init__(self, line):
        self.states = list()
        details, states = line.split("?")
        self.pattern, self.b, self.a = details.split(";")
        entry_state_unassigned = True
        for state_detail in states.split(";"):
            name, *transitions = state_detail.split(",")
            state = State(name, entry_state_unassigned)
            entry_state_unassigned = False
            for transition in transitions:
                inputs, output, next = transition.split(':')
                for input in inputs:
                    state.addTransition(input, output, next)
            self.states.append(state)
        self.print()

    def print(self):
        print("[" + self.pattern + "]")
        for state in self.states:
            print("(" + state.name + ") => ")
            for transition in state.transitions:
                print(transition.input + ":" + transition.output)

