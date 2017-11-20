def min_width_increasing(signature_sequence):
    n = len(signature_sequence)
    t_occurences = list()
    R = n
    C = n
    D = 0
    for symbol in signature_sequence:
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
    return min(R,C)
def min_width_peak(signature_sequence):
    n = len(signature_sequence)
    t_occurences = list()
    R = n
    C = n
    D = 0
    for symbol in signature_sequence:
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
    return min(R,C)
