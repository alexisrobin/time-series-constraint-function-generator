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
                current_state = 's'
            if symbol == '>':
                t_occurences.append('out')
                current_state = 's'
            if symbol == '=':
                t_occurences.append('out')
                current_state = 's'
    return t_occurences
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
                current_state = 'r'
            if symbol == '=':
                t_occurences.append('maybeb')
                current_state = 'r'
            if symbol == '>':
                t_occurences.append('found')
                current_state = 't'
        elif  current_state == 't':
            if symbol == '>':
                t_occurences.append('in')
                current_state = 't'
            if symbol == '=':
                t_occurences.append('maybea')
                current_state = 't'
            if symbol == '<':
                t_occurences.append('outa')
                current_state = 'r'
    return t_occurences
