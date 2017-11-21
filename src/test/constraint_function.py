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
                    c_tmp = c
                    d_tmp = 1
                    r_tmp = max(r,max(max(d,delta),deltaprime))
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 's'
                if symbol == '>':
                    c_tmp = c
                    d_tmp = d
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 's'
                if symbol == '=':
                    c_tmp = c
                    d_tmp = d
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
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
                    c_tmp = c
                    d_tmp = 0
                    r_tmp = max(r,d+delta+deltaprime)
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 's'
                if symbol == '>':
                    c_tmp = c
                    d_tmp = d
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 's'
                if symbol == '=':
                    c_tmp = c
                    d_tmp = d
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
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
                    c_tmp = c
                    d_tmp = 0
                    r_tmp = max(r,d+delta+deltaprime)
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 's'
                if symbol == '>':
                    c_tmp = c
                    d_tmp = d
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 's'
                if symbol == '=':
                    c_tmp = c
                    d_tmp = d
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
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
                    c_tmp = c
                    d_tmp = float('-inf')
                    r_tmp = max(r,max(max(d,delta),deltaprime))
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 's'
                if symbol == '>':
                    c_tmp = c
                    d_tmp = d
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 's'
                if symbol == '=':
                    c_tmp = c
                    d_tmp = d
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
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
                    c_tmp = c
                    d_tmp = float('inf')
                    r_tmp = max(r,min(min(d,delta),deltaprime))
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 's'
                if symbol == '>':
                    c_tmp = c
                    d_tmp = d
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 's'
                if symbol == '=':
                    c_tmp = c
                    d_tmp = d
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
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
                    c_tmp = c
                    h_tmp = deltaprime
                    r_tmp = max(r,abs(h-deltaprime))
                    c = c_tmp
                    h = h_tmp
                    r = r_tmp
                    current_state = 's'
                if symbol == '>':
                    c_tmp = c
                    h_tmp = deltaprime
                    r_tmp = r
                    c = c_tmp
                    h = h_tmp
                    r = r_tmp
                    current_state = 's'
                if symbol == '=':
                    c_tmp = c
                    h_tmp = deltaprime
                    r_tmp = r
                    c = c_tmp
                    h = h_tmp
                    r = r_tmp
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
                    c_tmp = c
                    d_tmp = 1
                    r_tmp = min(r,max(max(d,delta),deltaprime))
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 's'
                if symbol == '>':
                    c_tmp = c
                    d_tmp = d
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 's'
                if symbol == '=':
                    c_tmp = c
                    d_tmp = d
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
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
                    c_tmp = c
                    d_tmp = 0
                    r_tmp = min(r,d+delta+deltaprime)
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 's'
                if symbol == '>':
                    c_tmp = c
                    d_tmp = d
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 's'
                if symbol == '=':
                    c_tmp = c
                    d_tmp = d
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
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
                    c_tmp = c
                    d_tmp = 0
                    r_tmp = min(r,d+delta+deltaprime)
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 's'
                if symbol == '>':
                    c_tmp = c
                    d_tmp = d
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 's'
                if symbol == '=':
                    c_tmp = c
                    d_tmp = d
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
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
                    c_tmp = c
                    d_tmp = float('-inf')
                    r_tmp = min(r,max(max(d,delta),deltaprime))
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 's'
                if symbol == '>':
                    c_tmp = c
                    d_tmp = d
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 's'
                if symbol == '=':
                    c_tmp = c
                    d_tmp = d
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
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
                    c_tmp = c
                    d_tmp = float('inf')
                    r_tmp = min(r,min(min(d,delta),deltaprime))
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 's'
                if symbol == '>':
                    c_tmp = c
                    d_tmp = d
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 's'
                if symbol == '=':
                    c_tmp = c
                    d_tmp = d
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
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
                    c_tmp = c
                    h_tmp = deltaprime
                    r_tmp = min(r,abs(h-deltaprime))
                    c = c_tmp
                    h = h_tmp
                    r = r_tmp
                    current_state = 's'
                if symbol == '>':
                    c_tmp = c
                    h_tmp = deltaprime
                    r_tmp = r
                    c = c_tmp
                    h = h_tmp
                    r = r_tmp
                    current_state = 's'
                if symbol == '=':
                    c_tmp = c
                    h_tmp = deltaprime
                    r_tmp = r
                    c = c_tmp
                    h = h_tmp
                    r = r_tmp
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
                    c_tmp = c
                    d_tmp = 1
                    r_tmp = r+max(max(d,delta),deltaprime)
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 's'
                if symbol == '>':
                    c_tmp = c
                    d_tmp = d
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 's'
                if symbol == '=':
                    c_tmp = c
                    d_tmp = d
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
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
                    c_tmp = c
                    d_tmp = 0
                    r_tmp = r+d+delta+deltaprime
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 's'
                if symbol == '>':
                    c_tmp = c
                    d_tmp = d
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 's'
                if symbol == '=':
                    c_tmp = c
                    d_tmp = d
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
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
                    c_tmp = c
                    d_tmp = 0
                    r_tmp = r+d+delta+deltaprime
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 's'
                if symbol == '>':
                    c_tmp = c
                    d_tmp = d
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 's'
                if symbol == '=':
                    c_tmp = c
                    d_tmp = d
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
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
                    c_tmp = c
                    d_tmp = float('-inf')
                    r_tmp = r+max(max(d,delta),deltaprime)
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 's'
                if symbol == '>':
                    c_tmp = c
                    d_tmp = d
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 's'
                if symbol == '=':
                    c_tmp = c
                    d_tmp = d
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
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
                    c_tmp = c
                    d_tmp = float('inf')
                    r_tmp = r+min(min(d,delta),deltaprime)
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 's'
                if symbol == '>':
                    c_tmp = c
                    d_tmp = d
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 's'
                if symbol == '=':
                    c_tmp = c
                    d_tmp = d
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
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
                    c_tmp = c
                    h_tmp = deltaprime
                    r_tmp = r+abs(h-deltaprime)
                    c = c_tmp
                    h = h_tmp
                    r = r_tmp
                    current_state = 's'
                if symbol == '>':
                    c_tmp = c
                    h_tmp = deltaprime
                    r_tmp = r
                    c = c_tmp
                    h = h_tmp
                    r = r_tmp
                    current_state = 's'
                if symbol == '=':
                    c_tmp = c
                    h_tmp = deltaprime
                    r_tmp = r
                    c = c_tmp
                    h = h_tmp
                    r = r_tmp
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
                    c_tmp = c
                    d_tmp = d
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 's'
                if symbol == '=':
                    c_tmp = c
                    d_tmp = d
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 's'
                if symbol == '<':
                    c_tmp = c
                    d_tmp = d
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 'r'
            elif  current_state == 'r':
                if symbol == '<':
                    c_tmp = c
                    d_tmp = max(d,delta)
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 'r'
                if symbol == '=':
                    c_tmp = c
                    d_tmp = max(d,delta)
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 'r'
                if symbol == '>':
                    c_tmp = max(d,delta)
                    d_tmp = 1
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 't'
            elif  current_state == 't':
                if symbol == '>':
                    c_tmp = max(c,max(d,delta))
                    d_tmp = 1
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 't'
                if symbol == '=':
                    c_tmp = c
                    d_tmp = max(d,delta)
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 't'
                if symbol == '<':
                    c_tmp = 1
                    d_tmp = 1
                    r_tmp = max(r,c)
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
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
                    c_tmp = c
                    d_tmp = d
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 's'
                if symbol == '=':
                    c_tmp = c
                    d_tmp = d
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 's'
                if symbol == '<':
                    c_tmp = c
                    d_tmp = d
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 'r'
            elif  current_state == 'r':
                if symbol == '<':
                    c_tmp = c
                    d_tmp = d+delta
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 'r'
                if symbol == '=':
                    c_tmp = c
                    d_tmp = d+delta
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 'r'
                if symbol == '>':
                    c_tmp = d+delta
                    d_tmp = 0
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 't'
            elif  current_state == 't':
                if symbol == '>':
                    c_tmp = c+d+delta
                    d_tmp = 0
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 't'
                if symbol == '=':
                    c_tmp = c
                    d_tmp = d+delta
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 't'
                if symbol == '<':
                    c_tmp = 0
                    d_tmp = 0
                    r_tmp = max(r,c)
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
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
                    c_tmp = c
                    d_tmp = d
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 's'
                if symbol == '=':
                    c_tmp = c
                    d_tmp = d
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 's'
                if symbol == '<':
                    c_tmp = c
                    d_tmp = d
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 'r'
            elif  current_state == 'r':
                if symbol == '<':
                    c_tmp = c
                    d_tmp = d+delta
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 'r'
                if symbol == '=':
                    c_tmp = c
                    d_tmp = d+delta
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 'r'
                if symbol == '>':
                    c_tmp = d+delta
                    d_tmp = 0
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 't'
            elif  current_state == 't':
                if symbol == '>':
                    c_tmp = c+d+delta
                    d_tmp = 0
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 't'
                if symbol == '=':
                    c_tmp = c
                    d_tmp = d+delta
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 't'
                if symbol == '<':
                    c_tmp = float('-inf')
                    d_tmp = 0
                    r_tmp = max(r,c)
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
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
                    c_tmp = c
                    d_tmp = d
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 's'
                if symbol == '=':
                    c_tmp = c
                    d_tmp = d
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 's'
                if symbol == '<':
                    c_tmp = c
                    d_tmp = d
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 'r'
            elif  current_state == 'r':
                if symbol == '<':
                    c_tmp = c
                    d_tmp = max(d,delta)
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 'r'
                if symbol == '=':
                    c_tmp = c
                    d_tmp = max(d,delta)
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 'r'
                if symbol == '>':
                    c_tmp = max(d,delta)
                    d_tmp = float('-inf')
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 't'
            elif  current_state == 't':
                if symbol == '>':
                    c_tmp = max(c,max(d,delta))
                    d_tmp = float('-inf')
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 't'
                if symbol == '=':
                    c_tmp = c
                    d_tmp = max(d,delta)
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 't'
                if symbol == '<':
                    c_tmp = float('-inf')
                    d_tmp = float('-inf')
                    r_tmp = max(r,c)
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
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
                    c_tmp = c
                    d_tmp = d
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 's'
                if symbol == '=':
                    c_tmp = c
                    d_tmp = d
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 's'
                if symbol == '<':
                    c_tmp = c
                    d_tmp = d
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 'r'
            elif  current_state == 'r':
                if symbol == '<':
                    c_tmp = c
                    d_tmp = min(d,delta)
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 'r'
                if symbol == '=':
                    c_tmp = c
                    d_tmp = min(d,delta)
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 'r'
                if symbol == '>':
                    c_tmp = min(d,delta)
                    d_tmp = float('inf')
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 't'
            elif  current_state == 't':
                if symbol == '>':
                    c_tmp = min(c,min(d,delta))
                    d_tmp = float('inf')
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 't'
                if symbol == '=':
                    c_tmp = c
                    d_tmp = min(d,delta)
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 't'
                if symbol == '<':
                    c_tmp = float('-inf')
                    d_tmp = float('inf')
                    r_tmp = max(r,c)
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
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
                    c_tmp = c
                    h_tmp = deltaprime
                    r_tmp = r
                    c = c_tmp
                    h = h_tmp
                    r = r_tmp
                    current_state = 's'
                if symbol == '=':
                    c_tmp = c
                    h_tmp = deltaprime
                    r_tmp = r
                    c = c_tmp
                    h = h_tmp
                    r = r_tmp
                    current_state = 's'
                if symbol == '<':
                    c_tmp = c
                    h_tmp = deltaprime
                    r_tmp = r
                    c = c_tmp
                    h = h_tmp
                    r = r_tmp
                    current_state = 'r'
            elif  current_state == 'r':
                if symbol == '<':
                    c_tmp = c
                    h_tmp = h
                    r_tmp = r
                    c = c_tmp
                    h = h_tmp
                    r = r_tmp
                    current_state = 'r'
                if symbol == '=':
                    c_tmp = c
                    h_tmp = h
                    r_tmp = r
                    c = c_tmp
                    h = h_tmp
                    r = r_tmp
                    current_state = 'r'
                if symbol == '>':
                    c_tmp = abs(h-deltaprime)
                    h_tmp = h
                    r_tmp = r
                    c = c_tmp
                    h = h_tmp
                    r = r_tmp
                    current_state = 't'
            elif  current_state == 't':
                if symbol == '>':
                    c_tmp = abs(h-deltaprime)
                    h_tmp = h
                    r_tmp = r
                    c = c_tmp
                    h = h_tmp
                    r = r_tmp
                    current_state = 't'
                if symbol == '=':
                    c_tmp = c
                    h_tmp = h
                    r_tmp = r
                    c = c_tmp
                    h = h_tmp
                    r = r_tmp
                    current_state = 't'
                if symbol == '<':
                    c_tmp = 0
                    h_tmp = deltaprime
                    r_tmp = max(r,c)
                    c = c_tmp
                    h = h_tmp
                    r = r_tmp
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
                    c_tmp = c
                    d_tmp = d
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 's'
                if symbol == '=':
                    c_tmp = c
                    d_tmp = d
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 's'
                if symbol == '<':
                    c_tmp = c
                    d_tmp = d
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 'r'
            elif  current_state == 'r':
                if symbol == '<':
                    c_tmp = c
                    d_tmp = max(d,delta)
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 'r'
                if symbol == '=':
                    c_tmp = c
                    d_tmp = max(d,delta)
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 'r'
                if symbol == '>':
                    c_tmp = max(d,delta)
                    d_tmp = 1
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 't'
            elif  current_state == 't':
                if symbol == '>':
                    c_tmp = max(c,max(d,delta))
                    d_tmp = 1
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 't'
                if symbol == '=':
                    c_tmp = c
                    d_tmp = max(d,delta)
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 't'
                if symbol == '<':
                    c_tmp = 1
                    d_tmp = 1
                    r_tmp = min(r,c)
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
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
                    c_tmp = c
                    d_tmp = d
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 's'
                if symbol == '=':
                    c_tmp = c
                    d_tmp = d
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 's'
                if symbol == '<':
                    c_tmp = c
                    d_tmp = d
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 'r'
            elif  current_state == 'r':
                if symbol == '<':
                    c_tmp = c
                    d_tmp = d+delta
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 'r'
                if symbol == '=':
                    c_tmp = c
                    d_tmp = d+delta
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 'r'
                if symbol == '>':
                    c_tmp = d+delta
                    d_tmp = 0
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 't'
            elif  current_state == 't':
                if symbol == '>':
                    c_tmp = c+d+delta
                    d_tmp = 0
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 't'
                if symbol == '=':
                    c_tmp = c
                    d_tmp = d+delta
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 't'
                if symbol == '<':
                    c_tmp = n
                    d_tmp = 0
                    r_tmp = min(r,c)
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
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
                    c_tmp = c
                    d_tmp = d
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 's'
                if symbol == '=':
                    c_tmp = c
                    d_tmp = d
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 's'
                if symbol == '<':
                    c_tmp = c
                    d_tmp = d
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 'r'
            elif  current_state == 'r':
                if symbol == '<':
                    c_tmp = c
                    d_tmp = d+delta
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 'r'
                if symbol == '=':
                    c_tmp = c
                    d_tmp = d+delta
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 'r'
                if symbol == '>':
                    c_tmp = d+delta
                    d_tmp = 0
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 't'
            elif  current_state == 't':
                if symbol == '>':
                    c_tmp = c+d+delta
                    d_tmp = 0
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 't'
                if symbol == '=':
                    c_tmp = c
                    d_tmp = d+delta
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 't'
                if symbol == '<':
                    c_tmp = float('inf')
                    d_tmp = 0
                    r_tmp = min(r,c)
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
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
                    c_tmp = c
                    d_tmp = d
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 's'
                if symbol == '=':
                    c_tmp = c
                    d_tmp = d
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 's'
                if symbol == '<':
                    c_tmp = c
                    d_tmp = d
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 'r'
            elif  current_state == 'r':
                if symbol == '<':
                    c_tmp = c
                    d_tmp = max(d,delta)
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 'r'
                if symbol == '=':
                    c_tmp = c
                    d_tmp = max(d,delta)
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 'r'
                if symbol == '>':
                    c_tmp = max(d,delta)
                    d_tmp = float('-inf')
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 't'
            elif  current_state == 't':
                if symbol == '>':
                    c_tmp = max(c,max(d,delta))
                    d_tmp = float('-inf')
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 't'
                if symbol == '=':
                    c_tmp = c
                    d_tmp = max(d,delta)
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 't'
                if symbol == '<':
                    c_tmp = float('inf')
                    d_tmp = float('-inf')
                    r_tmp = min(r,c)
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
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
                    c_tmp = c
                    d_tmp = d
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 's'
                if symbol == '=':
                    c_tmp = c
                    d_tmp = d
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 's'
                if symbol == '<':
                    c_tmp = c
                    d_tmp = d
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 'r'
            elif  current_state == 'r':
                if symbol == '<':
                    c_tmp = c
                    d_tmp = min(d,delta)
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 'r'
                if symbol == '=':
                    c_tmp = c
                    d_tmp = min(d,delta)
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 'r'
                if symbol == '>':
                    c_tmp = min(d,delta)
                    d_tmp = float('inf')
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 't'
            elif  current_state == 't':
                if symbol == '>':
                    c_tmp = min(c,min(d,delta))
                    d_tmp = float('inf')
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 't'
                if symbol == '=':
                    c_tmp = c
                    d_tmp = min(d,delta)
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 't'
                if symbol == '<':
                    c_tmp = float('inf')
                    d_tmp = float('inf')
                    r_tmp = min(r,c)
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
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
                    c_tmp = c
                    h_tmp = deltaprime
                    r_tmp = r
                    c = c_tmp
                    h = h_tmp
                    r = r_tmp
                    current_state = 's'
                if symbol == '=':
                    c_tmp = c
                    h_tmp = deltaprime
                    r_tmp = r
                    c = c_tmp
                    h = h_tmp
                    r = r_tmp
                    current_state = 's'
                if symbol == '<':
                    c_tmp = c
                    h_tmp = deltaprime
                    r_tmp = r
                    c = c_tmp
                    h = h_tmp
                    r = r_tmp
                    current_state = 'r'
            elif  current_state == 'r':
                if symbol == '<':
                    c_tmp = c
                    h_tmp = h
                    r_tmp = r
                    c = c_tmp
                    h = h_tmp
                    r = r_tmp
                    current_state = 'r'
                if symbol == '=':
                    c_tmp = c
                    h_tmp = h
                    r_tmp = r
                    c = c_tmp
                    h = h_tmp
                    r = r_tmp
                    current_state = 'r'
                if symbol == '>':
                    c_tmp = abs(h-deltaprime)
                    h_tmp = h
                    r_tmp = r
                    c = c_tmp
                    h = h_tmp
                    r = r_tmp
                    current_state = 't'
            elif  current_state == 't':
                if symbol == '>':
                    c_tmp = abs(h-deltaprime)
                    h_tmp = h
                    r_tmp = r
                    c = c_tmp
                    h = h_tmp
                    r = r_tmp
                    current_state = 't'
                if symbol == '=':
                    c_tmp = c
                    h_tmp = h
                    r_tmp = r
                    c = c_tmp
                    h = h_tmp
                    r = r_tmp
                    current_state = 't'
                if symbol == '<':
                    c_tmp = float('inf')
                    h_tmp = deltaprime
                    r_tmp = min(r,c)
                    c = c_tmp
                    h = h_tmp
                    r = r_tmp
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
                    c_tmp = c
                    d_tmp = d
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 's'
                if symbol == '=':
                    c_tmp = c
                    d_tmp = d
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 's'
                if symbol == '<':
                    c_tmp = c
                    d_tmp = d
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 'r'
            elif  current_state == 'r':
                if symbol == '<':
                    c_tmp = c
                    d_tmp = max(d,delta)
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 'r'
                if symbol == '=':
                    c_tmp = c
                    d_tmp = max(d,delta)
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 'r'
                if symbol == '>':
                    c_tmp = max(d,delta)
                    d_tmp = 1
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 't'
            elif  current_state == 't':
                if symbol == '>':
                    c_tmp = max(c,max(d,delta))
                    d_tmp = 1
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 't'
                if symbol == '=':
                    c_tmp = c
                    d_tmp = max(d,delta)
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 't'
                if symbol == '<':
                    c_tmp = 0
                    d_tmp = 1
                    r_tmp = r+c
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
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
                    c_tmp = c
                    d_tmp = d
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 's'
                if symbol == '=':
                    c_tmp = c
                    d_tmp = d
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 's'
                if symbol == '<':
                    c_tmp = c
                    d_tmp = d
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 'r'
            elif  current_state == 'r':
                if symbol == '<':
                    c_tmp = c
                    d_tmp = d+delta
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 'r'
                if symbol == '=':
                    c_tmp = c
                    d_tmp = d+delta
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 'r'
                if symbol == '>':
                    c_tmp = d+delta
                    d_tmp = 0
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 't'
            elif  current_state == 't':
                if symbol == '>':
                    c_tmp = c+d+delta
                    d_tmp = 0
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 't'
                if symbol == '=':
                    c_tmp = c
                    d_tmp = d+delta
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 't'
                if symbol == '<':
                    c_tmp = 0
                    d_tmp = 0
                    r_tmp = r+c
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
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
                    c_tmp = c
                    d_tmp = d
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 's'
                if symbol == '=':
                    c_tmp = c
                    d_tmp = d
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 's'
                if symbol == '<':
                    c_tmp = c
                    d_tmp = d
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 'r'
            elif  current_state == 'r':
                if symbol == '<':
                    c_tmp = c
                    d_tmp = d+delta
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 'r'
                if symbol == '=':
                    c_tmp = c
                    d_tmp = d+delta
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 'r'
                if symbol == '>':
                    c_tmp = d+delta
                    d_tmp = 0
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 't'
            elif  current_state == 't':
                if symbol == '>':
                    c_tmp = c+d+delta
                    d_tmp = 0
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 't'
                if symbol == '=':
                    c_tmp = c
                    d_tmp = d+delta
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 't'
                if symbol == '<':
                    c_tmp = 0
                    d_tmp = 0
                    r_tmp = r+c
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
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
                    c_tmp = c
                    d_tmp = d
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 's'
                if symbol == '=':
                    c_tmp = c
                    d_tmp = d
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 's'
                if symbol == '<':
                    c_tmp = c
                    d_tmp = d
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 'r'
            elif  current_state == 'r':
                if symbol == '<':
                    c_tmp = c
                    d_tmp = max(d,delta)
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 'r'
                if symbol == '=':
                    c_tmp = c
                    d_tmp = max(d,delta)
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 'r'
                if symbol == '>':
                    c_tmp = max(d,delta)
                    d_tmp = float('-inf')
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 't'
            elif  current_state == 't':
                if symbol == '>':
                    c_tmp = max(c,max(d,delta))
                    d_tmp = float('-inf')
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 't'
                if symbol == '=':
                    c_tmp = c
                    d_tmp = max(d,delta)
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 't'
                if symbol == '<':
                    c_tmp = 0
                    d_tmp = float('-inf')
                    r_tmp = r+c
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
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
                    c_tmp = c
                    d_tmp = d
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 's'
                if symbol == '=':
                    c_tmp = c
                    d_tmp = d
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 's'
                if symbol == '<':
                    c_tmp = c
                    d_tmp = d
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 'r'
            elif  current_state == 'r':
                if symbol == '<':
                    c_tmp = c
                    d_tmp = min(d,delta)
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 'r'
                if symbol == '=':
                    c_tmp = c
                    d_tmp = min(d,delta)
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 'r'
                if symbol == '>':
                    c_tmp = min(d,delta)
                    d_tmp = float('inf')
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 't'
            elif  current_state == 't':
                if symbol == '>':
                    c_tmp = min(c,min(d,delta))
                    d_tmp = float('inf')
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 't'
                if symbol == '=':
                    c_tmp = c
                    d_tmp = min(d,delta)
                    r_tmp = r
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
                    current_state = 't'
                if symbol == '<':
                    c_tmp = 0
                    d_tmp = float('inf')
                    r_tmp = r+c
                    c = c_tmp
                    d = d_tmp
                    r = r_tmp
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
                    c_tmp = c
                    h_tmp = deltaprime
                    r_tmp = r
                    c = c_tmp
                    h = h_tmp
                    r = r_tmp
                    current_state = 's'
                if symbol == '=':
                    c_tmp = c
                    h_tmp = deltaprime
                    r_tmp = r
                    c = c_tmp
                    h = h_tmp
                    r = r_tmp
                    current_state = 's'
                if symbol == '<':
                    c_tmp = c
                    h_tmp = deltaprime
                    r_tmp = r
                    c = c_tmp
                    h = h_tmp
                    r = r_tmp
                    current_state = 'r'
            elif  current_state == 'r':
                if symbol == '<':
                    c_tmp = c
                    h_tmp = h
                    r_tmp = r
                    c = c_tmp
                    h = h_tmp
                    r = r_tmp
                    current_state = 'r'
                if symbol == '=':
                    c_tmp = c
                    h_tmp = h
                    r_tmp = r
                    c = c_tmp
                    h = h_tmp
                    r = r_tmp
                    current_state = 'r'
                if symbol == '>':
                    c_tmp = abs(h-deltaprime)
                    h_tmp = h
                    r_tmp = r
                    c = c_tmp
                    h = h_tmp
                    r = r_tmp
                    current_state = 't'
            elif  current_state == 't':
                if symbol == '>':
                    c_tmp = abs(h-deltaprime)
                    h_tmp = h
                    r_tmp = r
                    c = c_tmp
                    h = h_tmp
                    r = r_tmp
                    current_state = 't'
                if symbol == '=':
                    c_tmp = c
                    h_tmp = h
                    r_tmp = r
                    c = c_tmp
                    h = h_tmp
                    r = r_tmp
                    current_state = 't'
                if symbol == '<':
                    c_tmp = 0
                    h_tmp = deltaprime
                    r_tmp = r+c
                    c = c_tmp
                    h = h_tmp
                    r = r_tmp
                    current_state = 'r'
        previous_number = number
    return r+c

