def compute_signature_sequence(time_series):
    signature_sequence = list()
    for current_number in time_series:
        if 'last_number' in locals():
            if last_number > current_number:
                signature_sequence.append('>')
            elif last_number < current_number:
                signature_sequence.append('<')
            else:
                signature_sequence.append('=')
        last_number = current_number
    return signature_sequence

signature_sequence = compute_signature_sequence([4,4,2,2,3,5,5,6,3,1,1,2,2,2,2,2,2,1])
print(signature_sequence)



        

