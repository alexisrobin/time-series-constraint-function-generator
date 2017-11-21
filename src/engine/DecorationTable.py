import re
from . import util

class DecorationTable:

    INIT = "init"
    FINAL = "final"
    VARS = "vars"
    NO_AFTER = "_"
    AFTER_0 = "_-0"
    AFTER_1 = "_-1"

    def __init__(self, path):
        self.updates = {}
        functionRegex = r"(?P<function>\w+)\s?\((?P<args>.+)\)"
        regex = r",\s*(?![^()]*\))(?![^\[\]]*\])"
        lines = [line.rstrip('\n') for line in open(path)]
        for line in lines:
            attr = re.split(functionRegex, line)
            if(len(attr) > 2):
                attr = re.split(regex, attr[2])
                self.addToUpdates(attr[0],attr[1],attr[2],attr[4])

        print(self.updates)
        
    def addToUpdates(self, table_name, semantic_letter, after, value):

        if(after == "_-0"):
            after = "0"
        elif(after == "_-1"):
            after = "1"

        if table_name not in self.updates:
            self.updates[table_name] = {}
        
        if semantic_letter == DecorationTable.VARS:
            self.updates[table_name][semantic_letter] = re.findall(r"\w", value) #storing accumulators letter
        elif semantic_letter == DecorationTable.FINAL:
            self.updates[table_name][semantic_letter] = value
        else:
            if semantic_letter not in self.updates[table_name]:
                self.updates[table_name][semantic_letter] = {}
            if after not in self.updates[table_name][semantic_letter]:
                self.updates[table_name][semantic_letter][after] = {}

            value = value[1:-1] #removing '[]'
            values = util.top_level_split(value)
            for i, operation in enumerate(values):
                self.updates[table_name][semantic_letter][after][self.getAccumulatorLetterByIdx(table_name, i)] = operation

    def getAccumulatorLetterByIdx(self, table_name, idx):
        return self.updates[table_name][DecorationTable.VARS][idx]

    def getAccumulatorsLetter(self, table_name):
        return self.updates[table_name][DecorationTable.VARS]

    def getFinal(self, table_name):
        return self.updates[table_name][DecorationTable.FINAL]
    
    def getUpdate(self, table_name, semantic_letter, after, accumulator):
        try:
            return self.updates[table_name][semantic_letter][after][accumulator]
        except KeyError:
            if after == "0" or after == "1":
                return self.getUpdate(table_name, semantic_letter, "_", accumulator) # trying again with no after specified
            print("Error while finding update of " + accumulator + " in " + table_name + " decoration table for " + semantic_letter)