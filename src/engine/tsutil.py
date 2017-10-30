def signature_sequence(sequence):
    signature_sequence = list()
    for current_number in sequence:
        if 'last_number' in locals():
            if last_number > current_number:
                signature_sequence.append('>')
            elif last_number < current_number:
                signature_sequence.append('<')
            else:
                signature_sequence.append('=')
        last_number = current_number
    return signature_sequence
