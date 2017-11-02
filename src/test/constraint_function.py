def increasing(signature_sequence):
    t_occurences = list()
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
def peak(signature_sequence):
    t_occurences = list()
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
