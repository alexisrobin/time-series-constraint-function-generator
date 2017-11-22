def top_level_split(s):
    """
    Split `s` by top-level commas only. Commas within parentheses are ignored.
    """

    # Parse the string tracking whether the current character is within
    # parentheses.
    balanceParentheses = 0
    balanceBrackets = 0
    parts = []
    part = ''

    for c in s:
        part += c
        if c == '(':
            balanceParentheses += 1
        elif c == ')':
            balanceParentheses -= 1
        elif c == '[':
            balanceBrackets += 1
        elif c == ']':
            balanceBrackets -= 1
        elif c == ',' and balanceParentheses == 0 and balanceBrackets == 0:
            parts.append(part[:-1].strip())
            part = ''

    # Capture last part
    if len(part):
        parts.append(part.strip())

    return parts