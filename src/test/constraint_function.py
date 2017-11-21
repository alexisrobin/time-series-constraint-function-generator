def min_width_increasing(sequence):
    n = len(sequence)
    signature_sequence = list()
    t_occurences = list()
    aggregate = list()
    current = list()
    potential = list()
    R = n
    C = n
    D = 0
    for i, number in enumerate(sequence):
        if 'previous_number' in locals():
            if previous_number > number:
                symbol = '>'
            elif previous_number < number:
                symbol = '<'
            else:
                symbol = '='
            signature_sequence.append(symbol)
            if 'current_state' not in locals() or  current_state == 's':
                if symbol == '<':
                    t_occurences.append('founde')
                    R = min(R,D+1)
                    D = 0
                    current_state = 's'
                if symbol == '>':
                    t_occurences.append('out')
                    current_state = 's'
                if symbol == '=':
                    t_occurences.append('out')
                    current_state = 's'
        previous_number = number
        aggregate.append(R)
        current.append(C)
        potential.append(D)
    print(aggregate)
    print(current)
    print(potential)
    return min(R,C)
def min_surface_increasing(sequence):
    n = len(sequence)
    signature_sequence = list()
    t_occurences = list()
    aggregate = list()
    current = list()
    potential = list()
    R = float('inf')
    C = float('inf')
    D = 0
    for i, number in enumerate(sequence):
        if 'previous_number' in locals():
            if previous_number > number:
                symbol = '>'
            elif previous_number < number:
                symbol = '<'
            else:
                symbol = '='
            signature_sequence.append(symbol)
            if 'current_state' not in locals() or  current_state == 's':
                if symbol == '<':
                    t_occurences.append('founde')
                    R = min(R,D+sequence[i-1])
                    D = 0
                    current_state = 's'
                if symbol == '>':
                    t_occurences.append('out')
                    current_state = 's'
                if symbol == '=':
                    t_occurences.append('out')
                    current_state = 's'
        previous_number = number
        aggregate.append(R)
        current.append(C)
        potential.append(D)
    print(aggregate)
    print(current)
    print(potential)
    return min(R,C)
def min_max_increasing(sequence):
    n = len(sequence)
    signature_sequence = list()
    t_occurences = list()
    aggregate = list()
    current = list()
    potential = list()
    R = float('inf')
    C = float('inf')
    D = float('-inf')
    for i, number in enumerate(sequence):
        if 'previous_number' in locals():
            if previous_number > number:
                symbol = '>'
            elif previous_number < number:
                symbol = '<'
            else:
                symbol = '='
            signature_sequence.append(symbol)
            if 'current_state' not in locals() or  current_state == 's':
                if symbol == '<':
                    t_occurences.append('founde')
                    R = min(R,max(D,sequence[i-1]))
                    D = float('-inf')
                    current_state = 's'
                if symbol == '>':
                    t_occurences.append('out')
                    current_state = 's'
                if symbol == '=':
                    t_occurences.append('out')
                    current_state = 's'
        previous_number = number
        aggregate.append(R)
        current.append(C)
        potential.append(D)
    print(aggregate)
    print(current)
    print(potential)
    return min(R,C)
def min_min_increasing(sequence):
    n = len(sequence)
    signature_sequence = list()
    t_occurences = list()
    aggregate = list()
    current = list()
    potential = list()
    R = float('inf')
    C = float('inf')
    D = float('inf')
    for i, number in enumerate(sequence):
        if 'previous_number' in locals():
            if previous_number > number:
                symbol = '>'
            elif previous_number < number:
                symbol = '<'
            else:
                symbol = '='
            signature_sequence.append(symbol)
            if 'current_state' not in locals() or  current_state == 's':
                if symbol == '<':
                    t_occurences.append('founde')
                    R = min(R,min(D,sequence[i-1]))
                    D = float('inf')
                    current_state = 's'
                if symbol == '>':
                    t_occurences.append('out')
                    current_state = 's'
                if symbol == '=':
                    t_occurences.append('out')
                    current_state = 's'
        previous_number = number
        aggregate.append(R)
        current.append(C)
        potential.append(D)
    print(aggregate)
    print(current)
    print(potential)
    return min(R,C)
def min_width_peak(sequence):
    n = len(sequence)
    signature_sequence = list()
    t_occurences = list()
    aggregate = list()
    current = list()
    potential = list()
    R = n
    C = n
    D = 0
    for i, number in enumerate(sequence):
        if 'previous_number' in locals():
            if previous_number > number:
                symbol = '>'
            elif previous_number < number:
                symbol = '<'
            else:
                symbol = '='
            signature_sequence.append(symbol)
            if 'current_state' not in locals() or  current_state == 's':
                if symbol == '>':
                    t_occurences.append('out')
                    current_state = 's'
                if symbol == '=':
                    t_occurences.append('out')
                    current_state = 's'
                if symbol == '<':
                    t_occurences.append('out')
                    current_state = 'r'
            elif  current_state == 'r':
                if symbol == '<':
                    t_occurences.append('maybeb')
                    D = D+1
                    current_state = 'r'
                if symbol == '=':
                    t_occurences.append('maybeb')
                    D = D+1
                    current_state = 'r'
                if symbol == '>':
                    t_occurences.append('found')
                    C = D+1
                    D = 0
                    current_state = 't'
            elif  current_state == 't':
                if symbol == '>':
                    t_occurences.append('in')
                    C = C+D+1
                    D = 0
                    current_state = 't'
                if symbol == '=':
                    t_occurences.append('maybea')
                    D = D+1
                    current_state = 't'
                if symbol == '<':
                    t_occurences.append('outa')
                    R = min(R,C)
                    C = n
                    D = 0
                    current_state = 'r'
        previous_number = number
        aggregate.append(R)
        current.append(C)
        potential.append(D)
    print(aggregate)
    print(current)
    print(potential)
    return min(R,C)
def min_surface_peak(sequence):
    n = len(sequence)
    signature_sequence = list()
    t_occurences = list()
    aggregate = list()
    current = list()
    potential = list()
    R = float('inf')
    C = float('inf')
    D = 0
    for i, number in enumerate(sequence):
        if 'previous_number' in locals():
            if previous_number > number:
                symbol = '>'
            elif previous_number < number:
                symbol = '<'
            else:
                symbol = '='
            signature_sequence.append(symbol)
            if 'current_state' not in locals() or  current_state == 's':
                if symbol == '>':
                    t_occurences.append('out')
                    current_state = 's'
                if symbol == '=':
                    t_occurences.append('out')
                    current_state = 's'
                if symbol == '<':
                    t_occurences.append('out')
                    current_state = 'r'
            elif  current_state == 'r':
                if symbol == '<':
                    t_occurences.append('maybeb')
                    D = D+sequence[i-1]
                    current_state = 'r'
                if symbol == '=':
                    t_occurences.append('maybeb')
                    D = D+sequence[i-1]
                    current_state = 'r'
                if symbol == '>':
                    t_occurences.append('found')
                    C = D+sequence[i-1]
                    D = 0
                    current_state = 't'
            elif  current_state == 't':
                if symbol == '>':
                    t_occurences.append('in')
                    C = C+D+sequence[i-1]
                    D = 0
                    current_state = 't'
                if symbol == '=':
                    t_occurences.append('maybea')
                    D = D+sequence[i-1]
                    current_state = 't'
                if symbol == '<':
                    t_occurences.append('outa')
                    R = min(R,C)
                    C = float('inf')
                    D = 0
                    current_state = 'r'
        previous_number = number
        aggregate.append(R)
        current.append(C)
        potential.append(D)
    print(aggregate)
    print(current)
    print(potential)
    return min(R,C)
def min_max_peak(sequence):
    n = len(sequence)
    signature_sequence = list()
    t_occurences = list()
    aggregate = list()
    current = list()
    potential = list()
    R = float('inf')
    C = float('inf')
    D = float('-inf')
    for i, number in enumerate(sequence):
        if 'previous_number' in locals():
            if previous_number > number:
                symbol = '>'
            elif previous_number < number:
                symbol = '<'
            else:
                symbol = '='
            signature_sequence.append(symbol)
            if 'current_state' not in locals() or  current_state == 's':
                if symbol == '>':
                    t_occurences.append('out')
                    current_state = 's'
                if symbol == '=':
                    t_occurences.append('out')
                    current_state = 's'
                if symbol == '<':
                    t_occurences.append('out')
                    current_state = 'r'
            elif  current_state == 'r':
                if symbol == '<':
                    t_occurences.append('maybeb')
                    D = max(D,sequence[i-1])
                    current_state = 'r'
                if symbol == '=':
                    t_occurences.append('maybeb')
                    D = max(D,sequence[i-1])
                    current_state = 'r'
                if symbol == '>':
                    t_occurences.append('found')
                    C = max(D,sequence[i-1])
                    D = float('-inf')
                    current_state = 't'
            elif  current_state == 't':
                if symbol == '>':
                    t_occurences.append('in')
                    C = max(C,max(D,sequence[i-1]))
                    D = float('-inf')
                    current_state = 't'
                if symbol == '=':
                    t_occurences.append('maybea')
                    D = max(D,sequence[i-1])
                    current_state = 't'
                if symbol == '<':
                    t_occurences.append('outa')
                    R = min(R,C)
                    C = float('inf')
                    D = float('-inf')
                    current_state = 'r'
        previous_number = number
        aggregate.append(R)
        current.append(C)
        potential.append(D)
    print(aggregate)
    print(current)
    print(potential)
    return min(R,C)
def min_min_peak(sequence):
    n = len(sequence)
    signature_sequence = list()
    t_occurences = list()
    aggregate = list()
    current = list()
    potential = list()
    R = float('inf')
    C = float('inf')
    D = float('inf')
    for i, number in enumerate(sequence):
        if 'previous_number' in locals():
            if previous_number > number:
                symbol = '>'
            elif previous_number < number:
                symbol = '<'
            else:
                symbol = '='
            signature_sequence.append(symbol)
            if 'current_state' not in locals() or  current_state == 's':
                if symbol == '>':
                    t_occurences.append('out')
                    current_state = 's'
                if symbol == '=':
                    t_occurences.append('out')
                    current_state = 's'
                if symbol == '<':
                    t_occurences.append('out')
                    current_state = 'r'
            elif  current_state == 'r':
                if symbol == '<':
                    t_occurences.append('maybeb')
                    D = min(D,sequence[i-1])
                    current_state = 'r'
                if symbol == '=':
                    t_occurences.append('maybeb')
                    D = min(D,sequence[i-1])
                    current_state = 'r'
                if symbol == '>':
                    t_occurences.append('found')
                    C = min(D,sequence[i-1])
                    D = float('inf')
                    current_state = 't'
            elif  current_state == 't':
                if symbol == '>':
                    t_occurences.append('in')
                    C = min(C,min(D,sequence[i-1]))
                    D = float('inf')
                    current_state = 't'
                if symbol == '=':
                    t_occurences.append('maybea')
                    D = min(D,sequence[i-1])
                    current_state = 't'
                if symbol == '<':
                    t_occurences.append('outa')
                    R = min(R,C)
                    C = float('inf')
                    D = float('inf')
                    current_state = 'r'
        previous_number = number
        aggregate.append(R)
        current.append(C)
        potential.append(D)
    print(aggregate)
    print(current)
    print(potential)
    return min(R,C)
