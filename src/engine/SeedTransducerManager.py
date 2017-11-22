import re
from . import util

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

    def __init__(self, raw_seed):
        self.states = {}
        attr = util.top_level_split(raw_seed)
        self.pattern = attr[0]

        stateRegex = r"state\((.+?)\),"
        for raw_state in re.findall(stateRegex, attr[2]):
            state_attr = util.top_level_split(raw_state)
            if "initial" in state_attr[1]:
                s = State(state_attr[0], True)
                if("above" in state_attr[1]):
                    self.after = "0"
                else:
                    self.after = "1"
            else:
                s = State(state_attr[0])
            self.states[state_attr[0]] = s
        
        raw_arcs = util.top_level_split(attr[3][1:-1])
        for raw_arc in raw_arcs:
            arc_attr = util.top_level_split(raw_arc[4:-1])
            if "l" in arc_attr[1]:
                self.states[arc_attr[0]].addTransition("<", arc_attr[3], arc_attr[2])
            if "eq" in arc_attr[1]:
                self.states[arc_attr[0]].addTransition("=", arc_attr[3], arc_attr[2])
            if "g" in arc_attr[1]:
                self.states[arc_attr[0]].addTransition(">", arc_attr[3], arc_attr[2])

    def print(self):
        print("[" + self.pattern + "]")
        for state in self.states:
            print("(" + state.name + ") => ")
            for transition in state.transitions:
                print(transition.input + ":" + transition.output)

class SeedTransducerManager:

    def __init__(self, path):
        self.seed_transducers = {}
        lines = [line.rstrip('\n') for line in open(path)]
        file = ''.join(map(str, lines))
        file = file.replace('\t', '')
        file = file.replace(' ', '')
        seedRegex = r"seed_template\((.+?)\)\."
        seeds = re.findall(seedRegex, file)
        for seed in seeds:
            st = SeedTransducer(seed)
            self.seed_transducers[st.pattern] = st



