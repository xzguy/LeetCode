def isNumber(s):
    """
    :type s: str
    :rtype: bool
    """
    # define the DFA states transition table
    DFA_states = [
        {},
        # state(1): initial state 
        {'blank': 1, 'sign': 2, 'digit': 3, 'decimal_p': 4},
        # state(2): after sign, follow only digit or '.'
        {'digit': 3, 'decimal_p': 4},
        # state(3): after digit, follow only digit, '.', exp or end
        {'digit': 3, 'decimal_p': 5, 'exp': 6, 'blank': 9},
        # state(4): after '.', follow only digit
        {'digit': 5},
        # state(5): after digit. or .digit, follow only digit, exp or end
        {'digit': 5, 'exp': 6, 'blank': 9},
        # state(6): after exp, follow only sign or digit
        {'sign': 7, 'digit': 8},
        # state(7): after exp+sign, follow only digit
        {'digit': 8},
        # state(8): after everything, follow only digit or end
        {'digit': 8, 'blank': 9},
        # state(9) : successfully parsed
        {'blank': 9}
    ]
    current_state = 1
    # parse the input string
    for c in s:
        if c in '0123456789':
            c = 'digit'
        elif c in ' \t\n':
            c = 'blank'
        elif c in '+-':
            c = 'sign'
        elif c in 'eE':
            c = 'exp'
        elif c in '.':
            c = 'decimal_p'
        else:
            return False
        # invalid input for DFA
        if c not in DFA_states[current_state].keys():
            return False
        # state transition
        current_state = DFA_states[current_state][c]
    if current_state not in [3, 5, 8, 9]:
        return False
    return True

print(isNumber('+3.5e-5'))