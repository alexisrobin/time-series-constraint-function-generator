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
                    c = c
                    d = 1
                    r = max(r,max(max(d,0),0))
                    current_state = 's'
                if symbol == '>':
                    c = c
                    d = d
                    r = r
                    current_state = 's'
                if symbol == '=':
                    c = c
                    d = d
                    r = r
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
                    c = c
                    d = 0
                    r = max(r,d+1+1)
                    current_state = 's'
                if symbol == '>':
                    c = c
                    d = d
                    r = r
                    current_state = 's'
                if symbol == '=':
                    c = c
                    d = d
                    r = r
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
                    c = c
                    d = 0
                    r = max(r,d+sequence[i-1]+sequence[i])
                    current_state = 's'
                if symbol == '>':
                    c = c
                    d = d
                    r = r
                    current_state = 's'
                if symbol == '=':
                    c = c
                    d = d
                    r = r
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
                    c = c
                    d = float('-inf')
                    r = max(r,max(max(d,sequence[i-1]),sequence[i]))
                    current_state = 's'
                if symbol == '>':
                    c = c
                    d = d
                    r = r
                    current_state = 's'
                if symbol == '=':
                    c = c
                    d = d
                    r = r
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
                    c = c
                    d = float('inf')
                    r = max(r,min(min(d,sequence[i-1]),sequence[i]))
                    current_state = 's'
                if symbol == '>':
                    c = c
                    d = d
                    r = r
                    current_state = 's'
                if symbol == '=':
                    c = c
                    d = d
                    r = r
                    current_state = 's'
        previous_number = number
    return max(r,c)

def max_range_increasing(sequence):
    n = len(sequence)
    c=0
    h=sequence[0]
    r=0
    c_list = list()
    h_list = list()
    r_list = list()
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
                    c = c
                    h = sequence[i]
                    print(abs(h-deltaprime))
                    r = max(r,abs(h-deltaprime))
                    current_state = 's'
                if symbol == '>':
                    c = c
                    h = sequence[i]
                    r = r
                    current_state = 's'
                if symbol == '=':
                    c = c
                    h = sequence[i]
                    r = r
                    current_state = 's'
                c_list.append(c)
                h_list.append(h)
                r_list.append(r)
        previous_number = number
    print(c_list)
    print(h_list)
    print(r_list)
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
                    c = c
                    d = 1
                    r = min(r,max(max(d,0),0))
                    current_state = 's'
                if symbol == '>':
                    c = c
                    d = d
                    r = r
                    current_state = 's'
                if symbol == '=':
                    c = c
                    d = d
                    r = r
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
                    c = c
                    d = 0
                    r = min(r,d+1+1)
                    current_state = 's'
                if symbol == '>':
                    c = c
                    d = d
                    r = r
                    current_state = 's'
                if symbol == '=':
                    c = c
                    d = d
                    r = r
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
                    c = c
                    d = 0
                    r = min(r,d+sequence[i-1]+sequence[i])
                    current_state = 's'
                if symbol == '>':
                    c = c
                    d = d
                    r = r
                    current_state = 's'
                if symbol == '=':
                    c = c
                    d = d
                    r = r
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
                    c = c
                    d = float('-inf')
                    r = min(r,max(max(d,sequence[i-1]),sequence[i]))
                    current_state = 's'
                if symbol == '>':
                    c = c
                    d = d
                    r = r
                    current_state = 's'
                if symbol == '=':
                    c = c
                    d = d
                    r = r
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
                    c = c
                    d = float('inf')
                    r = min(r,min(min(d,sequence[i-1]),sequence[i]))
                    current_state = 's'
                if symbol == '>':
                    c = c
                    d = d
                    r = r
                    current_state = 's'
                if symbol == '=':
                    c = c
                    d = d
                    r = r
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
                    c = c
                    h = sequence[i]
                    r = min(r,abs(h-deltaprime))
                    current_state = 's'
                if symbol == '>':
                    c = c
                    h = sequence[i]
                    r = r
                    current_state = 's'
                if symbol == '=':
                    c = c
                    h = sequence[i]
                    r = r
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
                    c = c
                    d = 1
                    r = r+max(max(d,0),0)
                    current_state = 's'
                if symbol == '>':
                    c = c
                    d = d
                    r = r
                    current_state = 's'
                if symbol == '=':
                    c = c
                    d = d
                    r = r
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
                    c = c
                    d = 0
                    r = r+d+1+1
                    current_state = 's'
                if symbol == '>':
                    c = c
                    d = d
                    r = r
                    current_state = 's'
                if symbol == '=':
                    c = c
                    d = d
                    r = r
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
                    c = c
                    d = 0
                    r = r+d+sequence[i-1]+sequence[i]
                    current_state = 's'
                if symbol == '>':
                    c = c
                    d = d
                    r = r
                    current_state = 's'
                if symbol == '=':
                    c = c
                    d = d
                    r = r
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
                    c = c
                    d = float('-inf')
                    r = r+max(max(d,sequence[i-1]),sequence[i])
                    current_state = 's'
                if symbol == '>':
                    c = c
                    d = d
                    r = r
                    current_state = 's'
                if symbol == '=':
                    c = c
                    d = d
                    r = r
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
                    c = c
                    d = float('inf')
                    r = r+min(min(d,sequence[i-1]),sequence[i])
                    current_state = 's'
                if symbol == '>':
                    c = c
                    d = d
                    r = r
                    current_state = 's'
                if symbol == '=':
                    c = c
                    d = d
                    r = r
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
                    c = c
                    h = sequence[i]
                    r = r+abs(h-deltaprime)
                    current_state = 's'
                if symbol == '>':
                    c = c
                    h = sequence[i]
                    r = r
                    current_state = 's'
                if symbol == '=':
                    c = c
                    h = sequence[i]
                    r = r
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
                    c = c
                    d = d
                    r = r
                    current_state = 's'
                if symbol == '=':
                    c = c
                    d = d
                    r = r
                    current_state = 's'
                if symbol == '<':
                    c = c
                    d = d
                    r = r
                    current_state = 'r'
            elif  current_state == 'r':
                if symbol == '<':
                    c = c
                    d = max(d,0)
                    r = r
                    current_state = 'r'
                if symbol == '=':
                    c = c
                    d = max(d,0)
                    r = r
                    current_state = 'r'
                if symbol == '>':
                    c = max(d,0)
                    d = 1
                    r = r
                    current_state = 't'
            elif  current_state == 't':
                if symbol == '>':
                    c = max(c,max(d,0))
                    d = 1
                    r = r
                    current_state = 't'
                if symbol == '=':
                    c = c
                    d = max(d,0)
                    r = r
                    current_state = 't'
                if symbol == '<':
                    c = 1
                    d = 1
                    r = max(r,c)
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
                    c = c
                    d = d
                    r = r
                    current_state = 's'
                if symbol == '=':
                    c = c
                    d = d
                    r = r
                    current_state = 's'
                if symbol == '<':
                    c = c
                    d = d
                    r = r
                    current_state = 'r'
            elif  current_state == 'r':
                if symbol == '<':
                    c = c
                    d = d+1
                    r = r
                    current_state = 'r'
                if symbol == '=':
                    c = c
                    d = d+1
                    r = r
                    current_state = 'r'
                if symbol == '>':
                    c = d+1
                    d = 0
                    r = r
                    current_state = 't'
            elif  current_state == 't':
                if symbol == '>':
                    c = c+d+1
                    d = 0
                    r = r
                    current_state = 't'
                if symbol == '=':
                    c = c
                    d = d+1
                    r = r
                    current_state = 't'
                if symbol == '<':
                    c = 0
                    d = 0
                    r = max(r,c)
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
                    c = c
                    d = d
                    r = r
                    current_state = 's'
                if symbol == '=':
                    c = c
                    d = d
                    r = r
                    current_state = 's'
                if symbol == '<':
                    c = c
                    d = d
                    r = r
                    current_state = 'r'
            elif  current_state == 'r':
                if symbol == '<':
                    c = c
                    d = d+sequence[i-1]
                    r = r
                    current_state = 'r'
                if symbol == '=':
                    c = c
                    d = d+sequence[i-1]
                    r = r
                    current_state = 'r'
                if symbol == '>':
                    c = d+sequence[i-1]
                    d = 0
                    r = r
                    current_state = 't'
            elif  current_state == 't':
                if symbol == '>':
                    c = c+d+sequence[i-1]
                    d = 0
                    r = r
                    current_state = 't'
                if symbol == '=':
                    c = c
                    d = d+sequence[i-1]
                    r = r
                    current_state = 't'
                if symbol == '<':
                    c = float('-inf')
                    d = 0
                    r = max(r,c)
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
                    c = c
                    d = d
                    r = r
                    current_state = 's'
                if symbol == '=':
                    c = c
                    d = d
                    r = r
                    current_state = 's'
                if symbol == '<':
                    c = c
                    d = d
                    r = r
                    current_state = 'r'
            elif  current_state == 'r':
                if symbol == '<':
                    c = c
                    d = max(d,sequence[i-1])
                    r = r
                    current_state = 'r'
                if symbol == '=':
                    c = c
                    d = max(d,sequence[i-1])
                    r = r
                    current_state = 'r'
                if symbol == '>':
                    c = max(d,sequence[i-1])
                    d = float('-inf')
                    r = r
                    current_state = 't'
            elif  current_state == 't':
                if symbol == '>':
                    c = max(c,max(d,sequence[i-1]))
                    d = float('-inf')
                    r = r
                    current_state = 't'
                if symbol == '=':
                    c = c
                    d = max(d,sequence[i-1])
                    r = r
                    current_state = 't'
                if symbol == '<':
                    c = float('-inf')
                    d = float('-inf')
                    r = max(r,c)
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
                    c = c
                    d = d
                    r = r
                    current_state = 's'
                if symbol == '=':
                    c = c
                    d = d
                    r = r
                    current_state = 's'
                if symbol == '<':
                    c = c
                    d = d
                    r = r
                    current_state = 'r'
            elif  current_state == 'r':
                if symbol == '<':
                    c = c
                    d = min(d,sequence[i-1])
                    r = r
                    current_state = 'r'
                if symbol == '=':
                    c = c
                    d = min(d,sequence[i-1])
                    r = r
                    current_state = 'r'
                if symbol == '>':
                    c = min(d,sequence[i-1])
                    d = float('inf')
                    r = r
                    current_state = 't'
            elif  current_state == 't':
                if symbol == '>':
                    c = min(c,min(d,sequence[i-1]))
                    d = float('inf')
                    r = r
                    current_state = 't'
                if symbol == '=':
                    c = c
                    d = min(d,sequence[i-1])
                    r = r
                    current_state = 't'
                if symbol == '<':
                    c = float('-inf')
                    d = float('inf')
                    r = max(r,c)
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
                    c = c
                    h = sequence[i]
                    r = r
                    current_state = 's'
                if symbol == '=':
                    c = c
                    h = sequence[i]
                    r = r
                    current_state = 's'
                if symbol == '<':
                    c = c
                    h = sequence[i]
                    r = r
                    current_state = 'r'
            elif  current_state == 'r':
                if symbol == '<':
                    c = c
                    h = h
                    r = r
                    current_state = 'r'
                if symbol == '=':
                    c = c
                    h = h
                    r = r
                    current_state = 'r'
                if symbol == '>':
                    c = abs(h-deltaprime)
                    h = h
                    r = r
                    current_state = 't'
            elif  current_state == 't':
                if symbol == '>':
                    c = abs(h-deltaprime)
                    h = h
                    r = r
                    current_state = 't'
                if symbol == '=':
                    c = c
                    h = h
                    r = r
                    current_state = 't'
                if symbol == '<':
                    c = 0
                    h = sequence[i]
                    r = max(r,c)
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
                    c = c
                    d = d
                    r = r
                    current_state = 's'
                if symbol == '=':
                    c = c
                    d = d
                    r = r
                    current_state = 's'
                if symbol == '<':
                    c = c
                    d = d
                    r = r
                    current_state = 'r'
            elif  current_state == 'r':
                if symbol == '<':
                    c = c
                    d = max(d,0)
                    r = r
                    current_state = 'r'
                if symbol == '=':
                    c = c
                    d = max(d,0)
                    r = r
                    current_state = 'r'
                if symbol == '>':
                    c = max(d,0)
                    d = 1
                    r = r
                    current_state = 't'
            elif  current_state == 't':
                if symbol == '>':
                    c = max(c,max(d,0))
                    d = 1
                    r = r
                    current_state = 't'
                if symbol == '=':
                    c = c
                    d = max(d,0)
                    r = r
                    current_state = 't'
                if symbol == '<':
                    c = 1
                    d = 1
                    r = min(r,c)
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
                    c = c
                    d = d
                    r = r
                    current_state = 's'
                if symbol == '=':
                    c = c
                    d = d
                    r = r
                    current_state = 's'
                if symbol == '<':
                    c = c
                    d = d
                    r = r
                    current_state = 'r'
            elif  current_state == 'r':
                if symbol == '<':
                    c = c
                    d = d+1
                    r = r
                    current_state = 'r'
                if symbol == '=':
                    c = c
                    d = d+1
                    r = r
                    current_state = 'r'
                if symbol == '>':
                    c = d+1
                    d = 0
                    r = r
                    current_state = 't'
            elif  current_state == 't':
                if symbol == '>':
                    c = c+d+1
                    d = 0
                    r = r
                    current_state = 't'
                if symbol == '=':
                    c = c
                    d = d+1
                    r = r
                    current_state = 't'
                if symbol == '<':
                    c = n
                    d = 0
                    r = min(r,c)
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
                    c = c
                    d = d
                    r = r
                    current_state = 's'
                if symbol == '=':
                    c = c
                    d = d
                    r = r
                    current_state = 's'
                if symbol == '<':
                    c = c
                    d = d
                    r = r
                    current_state = 'r'
            elif  current_state == 'r':
                if symbol == '<':
                    c = c
                    d = d+sequence[i-1]
                    r = r
                    current_state = 'r'
                if symbol == '=':
                    c = c
                    d = d+sequence[i-1]
                    r = r
                    current_state = 'r'
                if symbol == '>':
                    c = d+sequence[i-1]
                    d = 0
                    r = r
                    current_state = 't'
            elif  current_state == 't':
                if symbol == '>':
                    c = c+d+sequence[i-1]
                    d = 0
                    r = r
                    current_state = 't'
                if symbol == '=':
                    c = c
                    d = d+sequence[i-1]
                    r = r
                    current_state = 't'
                if symbol == '<':
                    c = float('inf')
                    d = 0
                    r = min(r,c)
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
                    c = c
                    d = d
                    r = r
                    current_state = 's'
                if symbol == '=':
                    c = c
                    d = d
                    r = r
                    current_state = 's'
                if symbol == '<':
                    c = c
                    d = d
                    r = r
                    current_state = 'r'
            elif  current_state == 'r':
                if symbol == '<':
                    c = c
                    d = max(d,sequence[i-1])
                    r = r
                    current_state = 'r'
                if symbol == '=':
                    c = c
                    d = max(d,sequence[i-1])
                    r = r
                    current_state = 'r'
                if symbol == '>':
                    c = max(d,sequence[i-1])
                    d = float('-inf')
                    r = r
                    current_state = 't'
            elif  current_state == 't':
                if symbol == '>':
                    c = max(c,max(d,sequence[i-1]))
                    d = float('-inf')
                    r = r
                    current_state = 't'
                if symbol == '=':
                    c = c
                    d = max(d,sequence[i-1])
                    r = r
                    current_state = 't'
                if symbol == '<':
                    c = float('inf')
                    d = float('-inf')
                    r = min(r,c)
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
                    c = c
                    d = d
                    r = r
                    current_state = 's'
                if symbol == '=':
                    c = c
                    d = d
                    r = r
                    current_state = 's'
                if symbol == '<':
                    c = c
                    d = d
                    r = r
                    current_state = 'r'
            elif  current_state == 'r':
                if symbol == '<':
                    c = c
                    d = min(d,sequence[i-1])
                    r = r
                    current_state = 'r'
                if symbol == '=':
                    c = c
                    d = min(d,sequence[i-1])
                    r = r
                    current_state = 'r'
                if symbol == '>':
                    c = min(d,sequence[i-1])
                    d = float('inf')
                    r = r
                    current_state = 't'
            elif  current_state == 't':
                if symbol == '>':
                    c = min(c,min(d,sequence[i-1]))
                    d = float('inf')
                    r = r
                    current_state = 't'
                if symbol == '=':
                    c = c
                    d = min(d,sequence[i-1])
                    r = r
                    current_state = 't'
                if symbol == '<':
                    c = float('inf')
                    d = float('inf')
                    r = min(r,c)
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
                    c = c
                    h = sequence[i]
                    r = r
                    current_state = 's'
                if symbol == '=':
                    c = c
                    h = sequence[i]
                    r = r
                    current_state = 's'
                if symbol == '<':
                    c = c
                    h = sequence[i]
                    r = r
                    current_state = 'r'
            elif  current_state == 'r':
                if symbol == '<':
                    c = c
                    h = h
                    r = r
                    current_state = 'r'
                if symbol == '=':
                    c = c
                    h = h
                    r = r
                    current_state = 'r'
                if symbol == '>':
                    c = abs(h-deltaprime)
                    h = h
                    r = r
                    current_state = 't'
            elif  current_state == 't':
                if symbol == '>':
                    c = abs(h-deltaprime)
                    h = h
                    r = r
                    current_state = 't'
                if symbol == '=':
                    c = c
                    h = h
                    r = r
                    current_state = 't'
                if symbol == '<':
                    c = float('inf')
                    h = sequence[i]
                    r = min(r,c)
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
                    c = c
                    d = d
                    r = r
                    current_state = 's'
                if symbol == '=':
                    c = c
                    d = d
                    r = r
                    current_state = 's'
                if symbol == '<':
                    c = c
                    d = d
                    r = r
                    current_state = 'r'
            elif  current_state == 'r':
                if symbol == '<':
                    c = c
                    d = max(d,0)
                    r = r
                    current_state = 'r'
                if symbol == '=':
                    c = c
                    d = max(d,0)
                    r = r
                    current_state = 'r'
                if symbol == '>':
                    c = max(d,0)
                    d = 1
                    r = r
                    current_state = 't'
            elif  current_state == 't':
                if symbol == '>':
                    c = max(c,max(d,0))
                    d = 1
                    r = r
                    current_state = 't'
                if symbol == '=':
                    c = c
                    d = max(d,0)
                    r = r
                    current_state = 't'
                if symbol == '<':
                    c = 0
                    d = 1
                    r = r+c
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
                    c = c
                    d = d
                    r = r
                    current_state = 's'
                if symbol == '=':
                    c = c
                    d = d
                    r = r
                    current_state = 's'
                if symbol == '<':
                    c = c
                    d = d
                    r = r
                    current_state = 'r'
            elif  current_state == 'r':
                if symbol == '<':
                    c = c
                    d = d+1
                    r = r
                    current_state = 'r'
                if symbol == '=':
                    c = c
                    d = d+1
                    r = r
                    current_state = 'r'
                if symbol == '>':
                    c = d+1
                    d = 0
                    r = r
                    current_state = 't'
            elif  current_state == 't':
                if symbol == '>':
                    c = c+d+1
                    d = 0
                    r = r
                    current_state = 't'
                if symbol == '=':
                    c = c
                    d = d+1
                    r = r
                    current_state = 't'
                if symbol == '<':
                    c = 0
                    d = 0
                    r = r+c
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
                    c = c
                    d = d
                    r = r
                    current_state = 's'
                if symbol == '=':
                    c = c
                    d = d
                    r = r
                    current_state = 's'
                if symbol == '<':
                    c = c
                    d = d
                    r = r
                    current_state = 'r'
            elif  current_state == 'r':
                if symbol == '<':
                    c = c
                    d = d+sequence[i-1]
                    r = r
                    current_state = 'r'
                if symbol == '=':
                    c = c
                    d = d+sequence[i-1]
                    r = r
                    current_state = 'r'
                if symbol == '>':
                    c = d+sequence[i-1]
                    d = 0
                    r = r
                    current_state = 't'
            elif  current_state == 't':
                if symbol == '>':
                    c = c+d+sequence[i-1]
                    d = 0
                    r = r
                    current_state = 't'
                if symbol == '=':
                    c = c
                    d = d+sequence[i-1]
                    r = r
                    current_state = 't'
                if symbol == '<':
                    c = 0
                    d = 0
                    r = r+c
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
                    c = c
                    d = d
                    r = r
                    current_state = 's'
                if symbol == '=':
                    c = c
                    d = d
                    r = r
                    current_state = 's'
                if symbol == '<':
                    c = c
                    d = d
                    r = r
                    current_state = 'r'
            elif  current_state == 'r':
                if symbol == '<':
                    c = c
                    d = max(d,sequence[i-1])
                    r = r
                    current_state = 'r'
                if symbol == '=':
                    c = c
                    d = max(d,sequence[i-1])
                    r = r
                    current_state = 'r'
                if symbol == '>':
                    c = max(d,sequence[i-1])
                    d = float('-inf')
                    r = r
                    current_state = 't'
            elif  current_state == 't':
                if symbol == '>':
                    c = max(c,max(d,sequence[i-1]))
                    d = float('-inf')
                    r = r
                    current_state = 't'
                if symbol == '=':
                    c = c
                    d = max(d,sequence[i-1])
                    r = r
                    current_state = 't'
                if symbol == '<':
                    c = 0
                    d = float('-inf')
                    r = r+c
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
                    c = c
                    d = d
                    r = r
                    current_state = 's'
                if symbol == '=':
                    c = c
                    d = d
                    r = r
                    current_state = 's'
                if symbol == '<':
                    c = c
                    d = d
                    r = r
                    current_state = 'r'
            elif  current_state == 'r':
                if symbol == '<':
                    c = c
                    d = min(d,sequence[i-1])
                    r = r
                    current_state = 'r'
                if symbol == '=':
                    c = c
                    d = min(d,sequence[i-1])
                    r = r
                    current_state = 'r'
                if symbol == '>':
                    c = min(d,sequence[i-1])
                    d = float('inf')
                    r = r
                    current_state = 't'
            elif  current_state == 't':
                if symbol == '>':
                    c = min(c,min(d,sequence[i-1]))
                    d = float('inf')
                    r = r
                    current_state = 't'
                if symbol == '=':
                    c = c
                    d = min(d,sequence[i-1])
                    r = r
                    current_state = 't'
                if symbol == '<':
                    c = 0
                    d = float('inf')
                    r = r+c
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
                    c = c
                    h = sequence[i]
                    r = r
                    current_state = 's'
                if symbol == '=':
                    c = c
                    h = sequence[i]
                    r = r
                    current_state = 's'
                if symbol == '<':
                    c = c
                    h = sequence[i]
                    r = r
                    current_state = 'r'
            elif  current_state == 'r':
                if symbol == '<':
                    c = c
                    h = h
                    r = r
                    current_state = 'r'
                if symbol == '=':
                    c = c
                    h = h
                    r = r
                    current_state = 'r'
                if symbol == '>':
                    c = abs(h-deltaprime)
                    h = h
                    r = r
                    current_state = 't'
            elif  current_state == 't':
                if symbol == '>':
                    c = abs(h-deltaprime)
                    h = h
                    r = r
                    current_state = 't'
                if symbol == '=':
                    c = c
                    h = h
                    r = r
                    current_state = 't'
                if symbol == '<':
                    c = 0
                    h = sequence[i]
                    r = r+c
                    current_state = 'r'
        previous_number = number
    return r+c

