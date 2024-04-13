def successors(state):
    next_states = []
    for col in range(8):
        for row in range(8):
            if row != state[col]:
                next_state = list(state)
                next_state[col] = row
                next_states.append(next_state)
    return next_states