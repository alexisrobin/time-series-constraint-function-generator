class DecorationTable:

    semantic_letters = ['out','outr','outa','maybeb','maybea','founde','found','in']

    def __init__(self, path):
        self.updateOfR = {}
        self.updateOfC = {}
        self.updateOfD = {}

        lines = [line.rstrip('\n') for line in open(path)]
        for line in lines:
            semantic_letter, updates = line.split("/")
            for update in updates.split(":"):
                accumulator, operation = update.split("<-")
                if(accumulator == "R"):
                    self.updateOfR[semantic_letter] = operation
                elif(accumulator == "C"):
                    self.updateOfC[semantic_letter] = operation
                elif(accumulator == "D"):
                    self.updateOfD[semantic_letter] = operation
                else:
                    raise LookupError("Accumulator '" + accumulator + "' doesn't exist.")
    
    def getUpdate(self, accumulator, semantic_letter):
        if(accumulator == "C"):
            return self.updateOfC[semantic_letter]
        elif(accumulator == "D"):
            return self.updateOfD[semantic_letter]
        elif(accumulator == "R"):
            return self.updateOfR[semantic_letter]
        else:
            raise LookupError("Accumulator '" + accumulator + "' doesn't exist.")

    def hasUpdate(self, accumulator, semantic_letter):
        if(accumulator == "C"):
            return semantic_letter in self.updateOfC
        elif(accumulator == "D"):
            return semantic_letter in self.updateOfD
        elif(accumulator == "R"):
            return semantic_letter in self.updateOfR
        else:
            raise LookupError("Accumulator '" + accumulator + "' doesn't exist.")