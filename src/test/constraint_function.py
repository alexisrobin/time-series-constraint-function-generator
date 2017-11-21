def max_one_increasing(sequence):
    n = len(sequence)
    c=1
    d=1
    r=1
    for i, number in enumerate(sequence):
        if 'previous_number' in locals():
            if previous_number > number:
                symbol = '>'
            elif previous_number < number:
                symbol = '<'
            else:
                symbol = '='
            delta = sequence[i-1]
            deltaprime = sequence[i]
            if 'current_state' not in locals() or  current_state == 's':
                if symbol == '<':
                    c_new = c
                    d_new = 1
                    r_new = max(r,max(max(d,0),0))
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 's'
                if symbol == '>':
                    c_new = c
                    d_new = d
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 's'
                if symbol == '=':
                    c_new = c
                    d_new = d
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 's'
        previous_number = number
    return max(r,c)

def max_width_increasing(sequence):
    n = len(sequence)
    c=0
    d=0
    r=0
    for i, number in enumerate(sequence):
        if 'previous_number' in locals():
            if previous_number > number:
                symbol = '>'
            elif previous_number < number:
                symbol = '<'
            else:
                symbol = '='
            delta = sequence[i-1]
            deltaprime = sequence[i]
            if 'current_state' not in locals() or  current_state == 's':
                if symbol == '<':
                    c_new = c
                    d_new = 0
                    r_new = max(r,d+1+1)
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 's'
                if symbol == '>':
                    c_new = c
                    d_new = d
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 's'
                if symbol == '=':
                    c_new = c
                    d_new = d
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 's'
        previous_number = number
    return max(r,c)

def max_surface_increasing(sequence):
    n = len(sequence)
    c=float('-inf')
    d=0
    r=float('-inf')
    for i, number in enumerate(sequence):
        if 'previous_number' in locals():
            if previous_number > number:
                symbol = '>'
            elif previous_number < number:
                symbol = '<'
            else:
                symbol = '='
            delta = sequence[i-1]
            deltaprime = sequence[i]
            if 'current_state' not in locals() or  current_state == 's':
                if symbol == '<':
                    c_new = c
                    d_new = 0
                    r_new = max(r,d+sequence[i-1]+sequence[i])
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 's'
                if symbol == '>':
                    c_new = c
                    d_new = d
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 's'
                if symbol == '=':
                    c_new = c
                    d_new = d
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 's'
        previous_number = number
    return max(r,c)

def max_max_increasing(sequence):
    n = len(sequence)
    c=float('-inf')
    d=float('-inf')
    r=float('-inf')
    for i, number in enumerate(sequence):
        if 'previous_number' in locals():
            if previous_number > number:
                symbol = '>'
            elif previous_number < number:
                symbol = '<'
            else:
                symbol = '='
            delta = sequence[i-1]
            deltaprime = sequence[i]
            if 'current_state' not in locals() or  current_state == 's':
                if symbol == '<':
                    c_new = c
                    d_new = float('-inf')
                    r_new = max(r,max(max(d,sequence[i-1]),sequence[i]))
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 's'
                if symbol == '>':
                    c_new = c
                    d_new = d
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 's'
                if symbol == '=':
                    c_new = c
                    d_new = d
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 's'
        previous_number = number
    return max(r,c)

def max_min_increasing(sequence):
    n = len(sequence)
    c=float('-inf')
    d=float('inf')
    r=float('-inf')
    for i, number in enumerate(sequence):
        if 'previous_number' in locals():
            if previous_number > number:
                symbol = '>'
            elif previous_number < number:
                symbol = '<'
            else:
                symbol = '='
            delta = sequence[i-1]
            deltaprime = sequence[i]
            if 'current_state' not in locals() or  current_state == 's':
                if symbol == '<':
                    c_new = c
                    d_new = float('inf')
                    r_new = max(r,min(min(d,sequence[i-1]),sequence[i]))
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 's'
                if symbol == '>':
                    c_new = c
                    d_new = d
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 's'
                if symbol == '=':
                    c_new = c
                    d_new = d
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 's'
        previous_number = number
    return max(r,c)

def max_range_increasing(sequence):
    n = len(sequence)
    c=0
    h=sequence[0]
    r=0
    for i, number in enumerate(sequence):
        if 'previous_number' in locals():
            if previous_number > number:
                symbol = '>'
            elif previous_number < number:
                symbol = '<'
            else:
                symbol = '='
            delta = sequence[i-1]
            deltaprime = sequence[i]
            if 'current_state' not in locals() or  current_state == 's':
                if symbol == '<':
                    c_new = c
                    h_new = sequence[i]
                    r_new = max(r,abs(h-deltaprime))
                    c = c_new
                    h = h_new
                    r = r_new
                    current_state = 's'
                if symbol == '>':
                    c_new = c
                    h_new = sequence[i]
                    r_new = r
                    c = c_new
                    h = h_new
                    r = r_new
                    current_state = 's'
                if symbol == '=':
                    c_new = c
                    h_new = sequence[i]
                    r_new = r
                    c = c_new
                    h = h_new
                    r = r_new
                    current_state = 's'
        previous_number = number
    return max(r,c)

def min_one_increasing(sequence):
    n = len(sequence)
    c=1
    d=1
    r=1
    for i, number in enumerate(sequence):
        if 'previous_number' in locals():
            if previous_number > number:
                symbol = '>'
            elif previous_number < number:
                symbol = '<'
            else:
                symbol = '='
            delta = sequence[i-1]
            deltaprime = sequence[i]
            if 'current_state' not in locals() or  current_state == 's':
                if symbol == '<':
                    c_new = c
                    d_new = 1
                    r_new = min(r,max(max(d,0),0))
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 's'
                if symbol == '>':
                    c_new = c
                    d_new = d
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 's'
                if symbol == '=':
                    c_new = c
                    d_new = d
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 's'
        previous_number = number
    return min(r,c)

def min_width_increasing(sequence):
    n = len(sequence)
    c=n
    d=0
    r=n
    for i, number in enumerate(sequence):
        if 'previous_number' in locals():
            if previous_number > number:
                symbol = '>'
            elif previous_number < number:
                symbol = '<'
            else:
                symbol = '='
            delta = sequence[i-1]
            deltaprime = sequence[i]
            if 'current_state' not in locals() or  current_state == 's':
                if symbol == '<':
                    c_new = c
                    d_new = 0
                    r_new = min(r,d+1+1)
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 's'
                if symbol == '>':
                    c_new = c
                    d_new = d
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 's'
                if symbol == '=':
                    c_new = c
                    d_new = d
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 's'
        previous_number = number
    return min(r,c)

def min_surface_increasing(sequence):
    n = len(sequence)
    c=float('inf')
    d=0
    r=float('inf')
    for i, number in enumerate(sequence):
        if 'previous_number' in locals():
            if previous_number > number:
                symbol = '>'
            elif previous_number < number:
                symbol = '<'
            else:
                symbol = '='
            delta = sequence[i-1]
            deltaprime = sequence[i]
            if 'current_state' not in locals() or  current_state == 's':
                if symbol == '<':
                    c_new = c
                    d_new = 0
                    r_new = min(r,d+sequence[i-1]+sequence[i])
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 's'
                if symbol == '>':
                    c_new = c
                    d_new = d
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 's'
                if symbol == '=':
                    c_new = c
                    d_new = d
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 's'
        previous_number = number
    return min(r,c)

def min_max_increasing(sequence):
    n = len(sequence)
    c=float('inf')
    d=float('-inf')
    r=float('inf')
    for i, number in enumerate(sequence):
        if 'previous_number' in locals():
            if previous_number > number:
                symbol = '>'
            elif previous_number < number:
                symbol = '<'
            else:
                symbol = '='
            delta = sequence[i-1]
            deltaprime = sequence[i]
            if 'current_state' not in locals() or  current_state == 's':
                if symbol == '<':
                    c_new = c
                    d_new = float('-inf')
                    r_new = min(r,max(max(d,sequence[i-1]),sequence[i]))
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 's'
                if symbol == '>':
                    c_new = c
                    d_new = d
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 's'
                if symbol == '=':
                    c_new = c
                    d_new = d
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 's'
        previous_number = number
    return min(r,c)

def min_min_increasing(sequence):
    n = len(sequence)
    c=float('inf')
    d=float('inf')
    r=float('inf')
    for i, number in enumerate(sequence):
        if 'previous_number' in locals():
            if previous_number > number:
                symbol = '>'
            elif previous_number < number:
                symbol = '<'
            else:
                symbol = '='
            delta = sequence[i-1]
            deltaprime = sequence[i]
            if 'current_state' not in locals() or  current_state == 's':
                if symbol == '<':
                    c_new = c
                    d_new = float('inf')
                    r_new = min(r,min(min(d,sequence[i-1]),sequence[i]))
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 's'
                if symbol == '>':
                    c_new = c
                    d_new = d
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 's'
                if symbol == '=':
                    c_new = c
                    d_new = d
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 's'
        previous_number = number
    return min(r,c)

def min_range_increasing(sequence):
    n = len(sequence)
    c=float('inf')
    h=sequence[0]
    r=float('inf')
    for i, number in enumerate(sequence):
        if 'previous_number' in locals():
            if previous_number > number:
                symbol = '>'
            elif previous_number < number:
                symbol = '<'
            else:
                symbol = '='
            delta = sequence[i-1]
            deltaprime = sequence[i]
            if 'current_state' not in locals() or  current_state == 's':
                if symbol == '<':
                    c_new = c
                    h_new = sequence[i]
                    r_new = min(r,abs(h-deltaprime))
                    c = c_new
                    h = h_new
                    r = r_new
                    current_state = 's'
                if symbol == '>':
                    c_new = c
                    h_new = sequence[i]
                    r_new = r
                    c = c_new
                    h = h_new
                    r = r_new
                    current_state = 's'
                if symbol == '=':
                    c_new = c
                    h_new = sequence[i]
                    r_new = r
                    c = c_new
                    h = h_new
                    r = r_new
                    current_state = 's'
        previous_number = number
    return min(r,c)

def sum_one_increasing(sequence):
    n = len(sequence)
    c=0
    d=1
    r=0
    for i, number in enumerate(sequence):
        if 'previous_number' in locals():
            if previous_number > number:
                symbol = '>'
            elif previous_number < number:
                symbol = '<'
            else:
                symbol = '='
            delta = sequence[i-1]
            deltaprime = sequence[i]
            if 'current_state' not in locals() or  current_state == 's':
                if symbol == '<':
                    c_new = c
                    d_new = 1
                    r_new = r+max(max(d,0),0)
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 's'
                if symbol == '>':
                    c_new = c
                    d_new = d
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 's'
                if symbol == '=':
                    c_new = c
                    d_new = d
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 's'
        previous_number = number
    return r+c

def sum_width_increasing(sequence):
    n = len(sequence)
    c=0
    d=0
    r=0
    for i, number in enumerate(sequence):
        if 'previous_number' in locals():
            if previous_number > number:
                symbol = '>'
            elif previous_number < number:
                symbol = '<'
            else:
                symbol = '='
            delta = sequence[i-1]
            deltaprime = sequence[i]
            if 'current_state' not in locals() or  current_state == 's':
                if symbol == '<':
                    c_new = c
                    d_new = 0
                    r_new = r+d+1+1
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 's'
                if symbol == '>':
                    c_new = c
                    d_new = d
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 's'
                if symbol == '=':
                    c_new = c
                    d_new = d
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 's'
        previous_number = number
    return r+c

def sum_surface_increasing(sequence):
    n = len(sequence)
    c=0
    d=0
    r=0
    for i, number in enumerate(sequence):
        if 'previous_number' in locals():
            if previous_number > number:
                symbol = '>'
            elif previous_number < number:
                symbol = '<'
            else:
                symbol = '='
            delta = sequence[i-1]
            deltaprime = sequence[i]
            if 'current_state' not in locals() or  current_state == 's':
                if symbol == '<':
                    c_new = c
                    d_new = 0
                    r_new = r+d+sequence[i-1]+sequence[i]
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 's'
                if symbol == '>':
                    c_new = c
                    d_new = d
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 's'
                if symbol == '=':
                    c_new = c
                    d_new = d
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 's'
        previous_number = number
    return r+c

def sum_max_increasing(sequence):
    n = len(sequence)
    c=0
    d=float('-inf')
    r=0
    for i, number in enumerate(sequence):
        if 'previous_number' in locals():
            if previous_number > number:
                symbol = '>'
            elif previous_number < number:
                symbol = '<'
            else:
                symbol = '='
            delta = sequence[i-1]
            deltaprime = sequence[i]
            if 'current_state' not in locals() or  current_state == 's':
                if symbol == '<':
                    c_new = c
                    d_new = float('-inf')
                    r_new = r+max(max(d,sequence[i-1]),sequence[i])
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 's'
                if symbol == '>':
                    c_new = c
                    d_new = d
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 's'
                if symbol == '=':
                    c_new = c
                    d_new = d
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 's'
        previous_number = number
    return r+c

def sum_min_increasing(sequence):
    n = len(sequence)
    c=0
    d=float('inf')
    r=0
    for i, number in enumerate(sequence):
        if 'previous_number' in locals():
            if previous_number > number:
                symbol = '>'
            elif previous_number < number:
                symbol = '<'
            else:
                symbol = '='
            delta = sequence[i-1]
            deltaprime = sequence[i]
            if 'current_state' not in locals() or  current_state == 's':
                if symbol == '<':
                    c_new = c
                    d_new = float('inf')
                    r_new = r+min(min(d,sequence[i-1]),sequence[i])
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 's'
                if symbol == '>':
                    c_new = c
                    d_new = d
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 's'
                if symbol == '=':
                    c_new = c
                    d_new = d
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 's'
        previous_number = number
    return r+c

def sum_range_increasing(sequence):
    n = len(sequence)
    c=0
    h=sequence[0]
    r=0
    for i, number in enumerate(sequence):
        if 'previous_number' in locals():
            if previous_number > number:
                symbol = '>'
            elif previous_number < number:
                symbol = '<'
            else:
                symbol = '='
            delta = sequence[i-1]
            deltaprime = sequence[i]
            if 'current_state' not in locals() or  current_state == 's':
                if symbol == '<':
                    c_new = c
                    h_new = sequence[i]
                    r_new = r+abs(h-deltaprime)
                    c = c_new
                    h = h_new
                    r = r_new
                    current_state = 's'
                if symbol == '>':
                    c_new = c
                    h_new = sequence[i]
                    r_new = r
                    c = c_new
                    h = h_new
                    r = r_new
                    current_state = 's'
                if symbol == '=':
                    c_new = c
                    h_new = sequence[i]
                    r_new = r
                    c = c_new
                    h = h_new
                    r = r_new
                    current_state = 's'
        previous_number = number
    return r+c

def max_one_peak(sequence):
    n = len(sequence)
    c=1
    d=1
    r=1
    for i, number in enumerate(sequence):
        if 'previous_number' in locals():
            if previous_number > number:
                symbol = '>'
            elif previous_number < number:
                symbol = '<'
            else:
                symbol = '='
            delta = sequence[i-1]
            deltaprime = sequence[i]
            if 'current_state' not in locals() or  current_state == 's':
                if symbol == '>':
                    c_new = c
                    d_new = d
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 's'
                if symbol == '=':
                    c_new = c
                    d_new = d
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 's'
                if symbol == '<':
                    c_new = c
                    d_new = d
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 'r'
            elif  current_state == 'r':
                if symbol == '<':
                    c_new = c
                    d_new = max(d,0)
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 'r'
                if symbol == '=':
                    c_new = c
                    d_new = max(d,0)
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 'r'
                if symbol == '>':
                    c_new = max(d,0)
                    d_new = 1
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 't'
            elif  current_state == 't':
                if symbol == '>':
                    c_new = max(c,max(d,0))
                    d_new = 1
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 't'
                if symbol == '=':
                    c_new = c
                    d_new = max(d,0)
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 't'
                if symbol == '<':
                    c_new = 1
                    d_new = 1
                    r_new = max(r,c)
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 'r'
        previous_number = number
    return max(r,c)

def max_width_peak(sequence):
    n = len(sequence)
    c=0
    d=0
    r=0
    for i, number in enumerate(sequence):
        if 'previous_number' in locals():
            if previous_number > number:
                symbol = '>'
            elif previous_number < number:
                symbol = '<'
            else:
                symbol = '='
            delta = sequence[i-1]
            deltaprime = sequence[i]
            if 'current_state' not in locals() or  current_state == 's':
                if symbol == '>':
                    c_new = c
                    d_new = d
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 's'
                if symbol == '=':
                    c_new = c
                    d_new = d
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 's'
                if symbol == '<':
                    c_new = c
                    d_new = d
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 'r'
            elif  current_state == 'r':
                if symbol == '<':
                    c_new = c
                    d_new = d+1
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 'r'
                if symbol == '=':
                    c_new = c
                    d_new = d+1
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 'r'
                if symbol == '>':
                    c_new = d+1
                    d_new = 0
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 't'
            elif  current_state == 't':
                if symbol == '>':
                    c_new = c+d+1
                    d_new = 0
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 't'
                if symbol == '=':
                    c_new = c
                    d_new = d+1
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 't'
                if symbol == '<':
                    c_new = 0
                    d_new = 0
                    r_new = max(r,c)
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 'r'
        previous_number = number
    return max(r,c)

def max_surface_peak(sequence):
    n = len(sequence)
    c=float('-inf')
    d=0
    r=float('-inf')
    for i, number in enumerate(sequence):
        if 'previous_number' in locals():
            if previous_number > number:
                symbol = '>'
            elif previous_number < number:
                symbol = '<'
            else:
                symbol = '='
            delta = sequence[i-1]
            deltaprime = sequence[i]
            if 'current_state' not in locals() or  current_state == 's':
                if symbol == '>':
                    c_new = c
                    d_new = d
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 's'
                if symbol == '=':
                    c_new = c
                    d_new = d
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 's'
                if symbol == '<':
                    c_new = c
                    d_new = d
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 'r'
            elif  current_state == 'r':
                if symbol == '<':
                    c_new = c
                    d_new = d+sequence[i-1]
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 'r'
                if symbol == '=':
                    c_new = c
                    d_new = d+sequence[i-1]
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 'r'
                if symbol == '>':
                    c_new = d+sequence[i-1]
                    d_new = 0
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 't'
            elif  current_state == 't':
                if symbol == '>':
                    c_new = c+d+sequence[i-1]
                    d_new = 0
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 't'
                if symbol == '=':
                    c_new = c
                    d_new = d+sequence[i-1]
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 't'
                if symbol == '<':
                    c_new = float('-inf')
                    d_new = 0
                    r_new = max(r,c)
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 'r'
        previous_number = number
    return max(r,c)

def max_max_peak(sequence):
    n = len(sequence)
    c=float('-inf')
    d=float('-inf')
    r=float('-inf')
    for i, number in enumerate(sequence):
        if 'previous_number' in locals():
            if previous_number > number:
                symbol = '>'
            elif previous_number < number:
                symbol = '<'
            else:
                symbol = '='
            delta = sequence[i-1]
            deltaprime = sequence[i]
            if 'current_state' not in locals() or  current_state == 's':
                if symbol == '>':
                    c_new = c
                    d_new = d
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 's'
                if symbol == '=':
                    c_new = c
                    d_new = d
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 's'
                if symbol == '<':
                    c_new = c
                    d_new = d
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 'r'
            elif  current_state == 'r':
                if symbol == '<':
                    c_new = c
                    d_new = max(d,sequence[i-1])
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 'r'
                if symbol == '=':
                    c_new = c
                    d_new = max(d,sequence[i-1])
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 'r'
                if symbol == '>':
                    c_new = max(d,sequence[i-1])
                    d_new = float('-inf')
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 't'
            elif  current_state == 't':
                if symbol == '>':
                    c_new = max(c,max(d,sequence[i-1]))
                    d_new = float('-inf')
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 't'
                if symbol == '=':
                    c_new = c
                    d_new = max(d,sequence[i-1])
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 't'
                if symbol == '<':
                    c_new = float('-inf')
                    d_new = float('-inf')
                    r_new = max(r,c)
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 'r'
        previous_number = number
    return max(r,c)

def max_min_peak(sequence):
    n = len(sequence)
    c=float('-inf')
    d=float('inf')
    r=float('-inf')
    for i, number in enumerate(sequence):
        if 'previous_number' in locals():
            if previous_number > number:
                symbol = '>'
            elif previous_number < number:
                symbol = '<'
            else:
                symbol = '='
            delta = sequence[i-1]
            deltaprime = sequence[i]
            if 'current_state' not in locals() or  current_state == 's':
                if symbol == '>':
                    c_new = c
                    d_new = d
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 's'
                if symbol == '=':
                    c_new = c
                    d_new = d
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 's'
                if symbol == '<':
                    c_new = c
                    d_new = d
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 'r'
            elif  current_state == 'r':
                if symbol == '<':
                    c_new = c
                    d_new = min(d,sequence[i-1])
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 'r'
                if symbol == '=':
                    c_new = c
                    d_new = min(d,sequence[i-1])
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 'r'
                if symbol == '>':
                    c_new = min(d,sequence[i-1])
                    d_new = float('inf')
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 't'
            elif  current_state == 't':
                if symbol == '>':
                    c_new = min(c,min(d,sequence[i-1]))
                    d_new = float('inf')
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 't'
                if symbol == '=':
                    c_new = c
                    d_new = min(d,sequence[i-1])
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 't'
                if symbol == '<':
                    c_new = float('-inf')
                    d_new = float('inf')
                    r_new = max(r,c)
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 'r'
        previous_number = number
    return max(r,c)

def max_range_peak(sequence):
    n = len(sequence)
    c=0
    h=sequence[0]
    r=0
    for i, number in enumerate(sequence):
        if 'previous_number' in locals():
            if previous_number > number:
                symbol = '>'
            elif previous_number < number:
                symbol = '<'
            else:
                symbol = '='
            delta = sequence[i-1]
            deltaprime = sequence[i]
            if 'current_state' not in locals() or  current_state == 's':
                if symbol == '>':
                    c_new = c
                    h_new = sequence[i]
                    r_new = r
                    c = c_new
                    h = h_new
                    r = r_new
                    current_state = 's'
                if symbol == '=':
                    c_new = c
                    h_new = sequence[i]
                    r_new = r
                    c = c_new
                    h = h_new
                    r = r_new
                    current_state = 's'
                if symbol == '<':
                    c_new = c
                    h_new = sequence[i]
                    r_new = r
                    c = c_new
                    h = h_new
                    r = r_new
                    current_state = 'r'
            elif  current_state == 'r':
                if symbol == '<':
                    c_new = c
                    h_new = h
                    r_new = r
                    c = c_new
                    h = h_new
                    r = r_new
                    current_state = 'r'
                if symbol == '=':
                    c_new = c
                    h_new = h
                    r_new = r
                    c = c_new
                    h = h_new
                    r = r_new
                    current_state = 'r'
                if symbol == '>':
                    c_new = abs(h-deltaprime)
                    h_new = h
                    r_new = r
                    c = c_new
                    h = h_new
                    r = r_new
                    current_state = 't'
            elif  current_state == 't':
                if symbol == '>':
                    c_new = abs(h-deltaprime)
                    h_new = h
                    r_new = r
                    c = c_new
                    h = h_new
                    r = r_new
                    current_state = 't'
                if symbol == '=':
                    c_new = c
                    h_new = h
                    r_new = r
                    c = c_new
                    h = h_new
                    r = r_new
                    current_state = 't'
                if symbol == '<':
                    c_new = 0
                    h_new = sequence[i]
                    r_new = max(r,c)
                    c = c_new
                    h = h_new
                    r = r_new
                    current_state = 'r'
        previous_number = number
    return max(r,c)

def min_one_peak(sequence):
    n = len(sequence)
    c=1
    d=1
    r=1
    for i, number in enumerate(sequence):
        if 'previous_number' in locals():
            if previous_number > number:
                symbol = '>'
            elif previous_number < number:
                symbol = '<'
            else:
                symbol = '='
            delta = sequence[i-1]
            deltaprime = sequence[i]
            if 'current_state' not in locals() or  current_state == 's':
                if symbol == '>':
                    c_new = c
                    d_new = d
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 's'
                if symbol == '=':
                    c_new = c
                    d_new = d
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 's'
                if symbol == '<':
                    c_new = c
                    d_new = d
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 'r'
            elif  current_state == 'r':
                if symbol == '<':
                    c_new = c
                    d_new = max(d,0)
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 'r'
                if symbol == '=':
                    c_new = c
                    d_new = max(d,0)
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 'r'
                if symbol == '>':
                    c_new = max(d,0)
                    d_new = 1
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 't'
            elif  current_state == 't':
                if symbol == '>':
                    c_new = max(c,max(d,0))
                    d_new = 1
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 't'
                if symbol == '=':
                    c_new = c
                    d_new = max(d,0)
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 't'
                if symbol == '<':
                    c_new = 1
                    d_new = 1
                    r_new = min(r,c)
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 'r'
        previous_number = number
    return min(r,c)

def min_width_peak(sequence):
    n = len(sequence)
    c=n
    d=0
    r=n
    for i, number in enumerate(sequence):
        if 'previous_number' in locals():
            if previous_number > number:
                symbol = '>'
            elif previous_number < number:
                symbol = '<'
            else:
                symbol = '='
            delta = sequence[i-1]
            deltaprime = sequence[i]
            if 'current_state' not in locals() or  current_state == 's':
                if symbol == '>':
                    c_new = c
                    d_new = d
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 's'
                if symbol == '=':
                    c_new = c
                    d_new = d
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 's'
                if symbol == '<':
                    c_new = c
                    d_new = d
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 'r'
            elif  current_state == 'r':
                if symbol == '<':
                    c_new = c
                    d_new = d+1
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 'r'
                if symbol == '=':
                    c_new = c
                    d_new = d+1
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 'r'
                if symbol == '>':
                    c_new = d+1
                    d_new = 0
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 't'
            elif  current_state == 't':
                if symbol == '>':
                    c_new = c+d+1
                    d_new = 0
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 't'
                if symbol == '=':
                    c_new = c
                    d_new = d+1
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 't'
                if symbol == '<':
                    c_new = n
                    d_new = 0
                    r_new = min(r,c)
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 'r'
        previous_number = number
    return min(r,c)

def min_surface_peak(sequence):
    n = len(sequence)
    c=float('inf')
    d=0
    r=float('inf')
    for i, number in enumerate(sequence):
        if 'previous_number' in locals():
            if previous_number > number:
                symbol = '>'
            elif previous_number < number:
                symbol = '<'
            else:
                symbol = '='
            delta = sequence[i-1]
            deltaprime = sequence[i]
            if 'current_state' not in locals() or  current_state == 's':
                if symbol == '>':
                    c_new = c
                    d_new = d
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 's'
                if symbol == '=':
                    c_new = c
                    d_new = d
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 's'
                if symbol == '<':
                    c_new = c
                    d_new = d
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 'r'
            elif  current_state == 'r':
                if symbol == '<':
                    c_new = c
                    d_new = d+sequence[i-1]
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 'r'
                if symbol == '=':
                    c_new = c
                    d_new = d+sequence[i-1]
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 'r'
                if symbol == '>':
                    c_new = d+sequence[i-1]
                    d_new = 0
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 't'
            elif  current_state == 't':
                if symbol == '>':
                    c_new = c+d+sequence[i-1]
                    d_new = 0
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 't'
                if symbol == '=':
                    c_new = c
                    d_new = d+sequence[i-1]
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 't'
                if symbol == '<':
                    c_new = float('inf')
                    d_new = 0
                    r_new = min(r,c)
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 'r'
        previous_number = number
    return min(r,c)

def min_max_peak(sequence):
    n = len(sequence)
    c=float('inf')
    d=float('-inf')
    r=float('inf')
    for i, number in enumerate(sequence):
        if 'previous_number' in locals():
            if previous_number > number:
                symbol = '>'
            elif previous_number < number:
                symbol = '<'
            else:
                symbol = '='
            delta = sequence[i-1]
            deltaprime = sequence[i]
            if 'current_state' not in locals() or  current_state == 's':
                if symbol == '>':
                    c_new = c
                    d_new = d
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 's'
                if symbol == '=':
                    c_new = c
                    d_new = d
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 's'
                if symbol == '<':
                    c_new = c
                    d_new = d
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 'r'
            elif  current_state == 'r':
                if symbol == '<':
                    c_new = c
                    d_new = max(d,sequence[i-1])
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 'r'
                if symbol == '=':
                    c_new = c
                    d_new = max(d,sequence[i-1])
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 'r'
                if symbol == '>':
                    c_new = max(d,sequence[i-1])
                    d_new = float('-inf')
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 't'
            elif  current_state == 't':
                if symbol == '>':
                    c_new = max(c,max(d,sequence[i-1]))
                    d_new = float('-inf')
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 't'
                if symbol == '=':
                    c_new = c
                    d_new = max(d,sequence[i-1])
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 't'
                if symbol == '<':
                    c_new = float('inf')
                    d_new = float('-inf')
                    r_new = min(r,c)
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 'r'
        previous_number = number
    return min(r,c)

def min_min_peak(sequence):
    n = len(sequence)
    c=float('inf')
    d=float('inf')
    r=float('inf')
    for i, number in enumerate(sequence):
        if 'previous_number' in locals():
            if previous_number > number:
                symbol = '>'
            elif previous_number < number:
                symbol = '<'
            else:
                symbol = '='
            delta = sequence[i-1]
            deltaprime = sequence[i]
            if 'current_state' not in locals() or  current_state == 's':
                if symbol == '>':
                    c_new = c
                    d_new = d
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 's'
                if symbol == '=':
                    c_new = c
                    d_new = d
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 's'
                if symbol == '<':
                    c_new = c
                    d_new = d
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 'r'
            elif  current_state == 'r':
                if symbol == '<':
                    c_new = c
                    d_new = min(d,sequence[i-1])
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 'r'
                if symbol == '=':
                    c_new = c
                    d_new = min(d,sequence[i-1])
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 'r'
                if symbol == '>':
                    c_new = min(d,sequence[i-1])
                    d_new = float('inf')
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 't'
            elif  current_state == 't':
                if symbol == '>':
                    c_new = min(c,min(d,sequence[i-1]))
                    d_new = float('inf')
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 't'
                if symbol == '=':
                    c_new = c
                    d_new = min(d,sequence[i-1])
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 't'
                if symbol == '<':
                    c_new = float('inf')
                    d_new = float('inf')
                    r_new = min(r,c)
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 'r'
        previous_number = number
    return min(r,c)

def min_range_peak(sequence):
    n = len(sequence)
    c=float('inf')
    h=sequence[0]
    r=float('inf')
    for i, number in enumerate(sequence):
        if 'previous_number' in locals():
            if previous_number > number:
                symbol = '>'
            elif previous_number < number:
                symbol = '<'
            else:
                symbol = '='
            delta = sequence[i-1]
            deltaprime = sequence[i]
            if 'current_state' not in locals() or  current_state == 's':
                if symbol == '>':
                    c_new = c
                    h_new = sequence[i]
                    r_new = r
                    c = c_new
                    h = h_new
                    r = r_new
                    current_state = 's'
                if symbol == '=':
                    c_new = c
                    h_new = sequence[i]
                    r_new = r
                    c = c_new
                    h = h_new
                    r = r_new
                    current_state = 's'
                if symbol == '<':
                    c_new = c
                    h_new = sequence[i]
                    r_new = r
                    c = c_new
                    h = h_new
                    r = r_new
                    current_state = 'r'
            elif  current_state == 'r':
                if symbol == '<':
                    c_new = c
                    h_new = h
                    r_new = r
                    c = c_new
                    h = h_new
                    r = r_new
                    current_state = 'r'
                if symbol == '=':
                    c_new = c
                    h_new = h
                    r_new = r
                    c = c_new
                    h = h_new
                    r = r_new
                    current_state = 'r'
                if symbol == '>':
                    c_new = abs(h-deltaprime)
                    h_new = h
                    r_new = r
                    c = c_new
                    h = h_new
                    r = r_new
                    current_state = 't'
            elif  current_state == 't':
                if symbol == '>':
                    c_new = abs(h-deltaprime)
                    h_new = h
                    r_new = r
                    c = c_new
                    h = h_new
                    r = r_new
                    current_state = 't'
                if symbol == '=':
                    c_new = c
                    h_new = h
                    r_new = r
                    c = c_new
                    h = h_new
                    r = r_new
                    current_state = 't'
                if symbol == '<':
                    c_new = float('inf')
                    h_new = sequence[i]
                    r_new = min(r,c)
                    c = c_new
                    h = h_new
                    r = r_new
                    current_state = 'r'
        previous_number = number
    return min(r,c)

def sum_one_peak(sequence):
    n = len(sequence)
    c=0
    d=1
    r=0
    for i, number in enumerate(sequence):
        if 'previous_number' in locals():
            if previous_number > number:
                symbol = '>'
            elif previous_number < number:
                symbol = '<'
            else:
                symbol = '='
            delta = sequence[i-1]
            deltaprime = sequence[i]
            if 'current_state' not in locals() or  current_state == 's':
                if symbol == '>':
                    c_new = c
                    d_new = d
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 's'
                if symbol == '=':
                    c_new = c
                    d_new = d
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 's'
                if symbol == '<':
                    c_new = c
                    d_new = d
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 'r'
            elif  current_state == 'r':
                if symbol == '<':
                    c_new = c
                    d_new = max(d,0)
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 'r'
                if symbol == '=':
                    c_new = c
                    d_new = max(d,0)
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 'r'
                if symbol == '>':
                    c_new = max(d,0)
                    d_new = 1
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 't'
            elif  current_state == 't':
                if symbol == '>':
                    c_new = max(c,max(d,0))
                    d_new = 1
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 't'
                if symbol == '=':
                    c_new = c
                    d_new = max(d,0)
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 't'
                if symbol == '<':
                    c_new = 0
                    d_new = 1
                    r_new = r+c
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 'r'
        previous_number = number
    return r+c

def sum_width_peak(sequence):
    n = len(sequence)
    c=0
    d=0
    r=0
    for i, number in enumerate(sequence):
        if 'previous_number' in locals():
            if previous_number > number:
                symbol = '>'
            elif previous_number < number:
                symbol = '<'
            else:
                symbol = '='
            delta = sequence[i-1]
            deltaprime = sequence[i]
            if 'current_state' not in locals() or  current_state == 's':
                if symbol == '>':
                    c_new = c
                    d_new = d
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 's'
                if symbol == '=':
                    c_new = c
                    d_new = d
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 's'
                if symbol == '<':
                    c_new = c
                    d_new = d
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 'r'
            elif  current_state == 'r':
                if symbol == '<':
                    c_new = c
                    d_new = d+1
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 'r'
                if symbol == '=':
                    c_new = c
                    d_new = d+1
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 'r'
                if symbol == '>':
                    c_new = d+1
                    d_new = 0
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 't'
            elif  current_state == 't':
                if symbol == '>':
                    c_new = c+d+1
                    d_new = 0
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 't'
                if symbol == '=':
                    c_new = c
                    d_new = d+1
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 't'
                if symbol == '<':
                    c_new = 0
                    d_new = 0
                    r_new = r+c
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 'r'
        previous_number = number
    return r+c

def sum_surface_peak(sequence):
    n = len(sequence)
    c=0
    d=0
    r=0
    for i, number in enumerate(sequence):
        if 'previous_number' in locals():
            if previous_number > number:
                symbol = '>'
            elif previous_number < number:
                symbol = '<'
            else:
                symbol = '='
            delta = sequence[i-1]
            deltaprime = sequence[i]
            if 'current_state' not in locals() or  current_state == 's':
                if symbol == '>':
                    c_new = c
                    d_new = d
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 's'
                if symbol == '=':
                    c_new = c
                    d_new = d
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 's'
                if symbol == '<':
                    c_new = c
                    d_new = d
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 'r'
            elif  current_state == 'r':
                if symbol == '<':
                    c_new = c
                    d_new = d+sequence[i-1]
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 'r'
                if symbol == '=':
                    c_new = c
                    d_new = d+sequence[i-1]
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 'r'
                if symbol == '>':
                    c_new = d+sequence[i-1]
                    d_new = 0
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 't'
            elif  current_state == 't':
                if symbol == '>':
                    c_new = c+d+sequence[i-1]
                    d_new = 0
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 't'
                if symbol == '=':
                    c_new = c
                    d_new = d+sequence[i-1]
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 't'
                if symbol == '<':
                    c_new = 0
                    d_new = 0
                    r_new = r+c
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 'r'
        previous_number = number
    return r+c

def sum_max_peak(sequence):
    n = len(sequence)
    c=0
    d=float('-inf')
    r=0
    for i, number in enumerate(sequence):
        if 'previous_number' in locals():
            if previous_number > number:
                symbol = '>'
            elif previous_number < number:
                symbol = '<'
            else:
                symbol = '='
            delta = sequence[i-1]
            deltaprime = sequence[i]
            if 'current_state' not in locals() or  current_state == 's':
                if symbol == '>':
                    c_new = c
                    d_new = d
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 's'
                if symbol == '=':
                    c_new = c
                    d_new = d
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 's'
                if symbol == '<':
                    c_new = c
                    d_new = d
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 'r'
            elif  current_state == 'r':
                if symbol == '<':
                    c_new = c
                    d_new = max(d,sequence[i-1])
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 'r'
                if symbol == '=':
                    c_new = c
                    d_new = max(d,sequence[i-1])
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 'r'
                if symbol == '>':
                    c_new = max(d,sequence[i-1])
                    d_new = float('-inf')
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 't'
            elif  current_state == 't':
                if symbol == '>':
                    c_new = max(c,max(d,sequence[i-1]))
                    d_new = float('-inf')
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 't'
                if symbol == '=':
                    c_new = c
                    d_new = max(d,sequence[i-1])
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 't'
                if symbol == '<':
                    c_new = 0
                    d_new = float('-inf')
                    r_new = r+c
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 'r'
        previous_number = number
    return r+c

def sum_min_peak(sequence):
    n = len(sequence)
    c=0
    d=float('inf')
    r=0
    for i, number in enumerate(sequence):
        if 'previous_number' in locals():
            if previous_number > number:
                symbol = '>'
            elif previous_number < number:
                symbol = '<'
            else:
                symbol = '='
            delta = sequence[i-1]
            deltaprime = sequence[i]
            if 'current_state' not in locals() or  current_state == 's':
                if symbol == '>':
                    c_new = c
                    d_new = d
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 's'
                if symbol == '=':
                    c_new = c
                    d_new = d
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 's'
                if symbol == '<':
                    c_new = c
                    d_new = d
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 'r'
            elif  current_state == 'r':
                if symbol == '<':
                    c_new = c
                    d_new = min(d,sequence[i-1])
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 'r'
                if symbol == '=':
                    c_new = c
                    d_new = min(d,sequence[i-1])
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 'r'
                if symbol == '>':
                    c_new = min(d,sequence[i-1])
                    d_new = float('inf')
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 't'
            elif  current_state == 't':
                if symbol == '>':
                    c_new = min(c,min(d,sequence[i-1]))
                    d_new = float('inf')
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 't'
                if symbol == '=':
                    c_new = c
                    d_new = min(d,sequence[i-1])
                    r_new = r
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 't'
                if symbol == '<':
                    c_new = 0
                    d_new = float('inf')
                    r_new = r+c
                    c = c_new
                    d = d_new
                    r = r_new
                    current_state = 'r'
        previous_number = number
    return r+c

def sum_range_peak(sequence):
    n = len(sequence)
    c=0
    h=sequence[0]
    r=0
    for i, number in enumerate(sequence):
        if 'previous_number' in locals():
            if previous_number > number:
                symbol = '>'
            elif previous_number < number:
                symbol = '<'
            else:
                symbol = '='
            delta = sequence[i-1]
            deltaprime = sequence[i]
            if 'current_state' not in locals() or  current_state == 's':
                if symbol == '>':
                    c_new = c
                    h_new = sequence[i]
                    r_new = r
                    c = c_new
                    h = h_new
                    r = r_new
                    current_state = 's'
                if symbol == '=':
                    c_new = c
                    h_new = sequence[i]
                    r_new = r
                    c = c_new
                    h = h_new
                    r = r_new
                    current_state = 's'
                if symbol == '<':
                    c_new = c
                    h_new = sequence[i]
                    r_new = r
                    c = c_new
                    h = h_new
                    r = r_new
                    current_state = 'r'
            elif  current_state == 'r':
                if symbol == '<':
                    c_new = c
                    h_new = h
                    r_new = r
                    c = c_new
                    h = h_new
                    r = r_new
                    current_state = 'r'
                if symbol == '=':
                    c_new = c
                    h_new = h
                    r_new = r
                    c = c_new
                    h = h_new
                    r = r_new
                    current_state = 'r'
                if symbol == '>':
                    c_new = abs(h-deltaprime)
                    h_new = h
                    r_new = r
                    c = c_new
                    h = h_new
                    r = r_new
                    current_state = 't'
            elif  current_state == 't':
                if symbol == '>':
                    c_new = abs(h-deltaprime)
                    h_new = h
                    r_new = r
                    c = c_new
                    h = h_new
                    r = r_new
                    current_state = 't'
                if symbol == '=':
                    c_new = c
                    h_new = h
                    r_new = r
                    c = c_new
                    h = h_new
                    r = r_new
                    current_state = 't'
                if symbol == '<':
                    c_new = 0
                    h_new = sequence[i]
                    r_new = r+c
                    c = c_new
                    h = h_new
                    r = r_new
                    current_state = 'r'
        previous_number = number
    return r+c

