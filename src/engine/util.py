def top_level_split(s):
    """
    Split `s` by top-level commas only. Commas within parentheses are ignored.
    """

    # Parse the string tracking whether the current character is within
    # parentheses.
    balance = 0
    parts = []
    part = ''

    for c in s:
        part += c
        if c == '(':
            balance += 1
        elif c == ')':
            balance -= 1
        elif c == ',' and balance == 0:
            parts.append(part[:-1].strip())
            part = ''

    # Capture last part
    if len(part):
        parts.append(part.strip())

    return parts