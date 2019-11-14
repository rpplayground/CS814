def minimax_value(state):
    # Check if one of four terminal states has been reached:
    if state in [([1], 1), ([], 2)]:
        v = -1
    elif state in [([1], 2), ([], 1)]:
        v = 1
    else
        # We are not at a terminal state so set up v and then call the successors
          
    # Unpack the state which is in the form of a tuple
    current_state_of_piles = state[0]
    player = state[1]
    return v

