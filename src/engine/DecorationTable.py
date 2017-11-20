class DecorationTable:

    semantic_letters = ['out','outr','outa','maybeb','maybea','founde','found','in']

    def __init__(self, path):
        updateOfR = {}
        updateOfC = {}
        updateOfD = {}

        lines = [line.rstrip('\n') for line in open(path)]
        for line in lines:
            semantic_letter, updates = line.split("/")
            for update in updates.split(":"):
                accumulator, operation = update.split("<-")
                if(accumulator == "R"):
                    updateOfR[semantic_letter] = operation
                elif(accumulator == "C"):
                    updateOfC[semantic_letter] = operation
                elif(accumulator == "D"):
                    updateOfD[semantic_letter] = operation
                else:
                    raise LookupError("Accumulator '" + accumulator + "' doesn't exist.")

