#%%
import time

#%%
def successors(state, depth):
    # Unpack the state which is in the form of a tuple
    piles = state[0]
    player = state[1]
    # Flip the next player
    if player == 1:
        next_player = 2
    else:
        next_player = 1

    # We can pick either 3, 2 or 1 sticks from only one of piles
    successors = []
    all_new_piles = []
    for pile_index, pile in enumerate(piles):
        for pick in [1, 2, 3]:
            if pile >= pick:
                result = pile - pick
                if result != 0:
                    new_piles = sorted(piles[:pile_index] + [result] + piles[pile_index + 1:])
                else:
                    new_piles = sorted(piles[:pile_index] + piles[pile_index + 1:])
                all_new_piles.append(new_piles)
    # Check for duplicates...
    # See second answer in Stack Overflow page : https://stackoverflow.com/questions/2213923/removing-duplicates-from-a-list-of-lists
    all_new_piles = sorted(all_new_piles)
    successors = [(all_new_piles[i], next_player) for i in range(len(all_new_piles))\
        if i == 0 or all_new_piles[i] != all_new_piles[i-1]]
    print("--- Depth: " + str(depth) + " ---State: " + str(state))
    print(successors)
    return successors

#%%
def terminal_test(state):
    # Check if one of four terminal states has been reached:
    if state in [([1], 1), ([], 2)]:
        terminal_state = True
        utility_value = -1
    elif state in [([1], 2), ([], 1)]:
        terminal_state = True
        utility_value = 1
    else:
        terminal_state = False
        if state[1] == 1:
            utility_value = -1
        else:
            utility_value = 1
    return terminal_state, utility_value

#%% [markdown]
## Vanilla Minimax Functions

#%%
def max_value(state, depth):
    # Check if one of four terminal states has been reached:
    terminal_state, utility_value = terminal_test(state)
    if not terminal_state:
        depth = depth + 1
        for next_state in successors(state, depth):
            v_ = min_value(next_state, depth)
            if v_ > utility_value:
                utility_value = v_
    return utility_value

#%%
def min_value(state, depth):
    # Check if one of four terminal states has been reached:
    terminal_state, utility_value = terminal_test(state)
    if not terminal_state:
        depth = depth + 1
        for next_state in successors(state, depth):
            v_ = max_value(next_state, depth)
            if v_ < utility_value:
                utility_value = v_
    return utility_value

#%%
def minimax_value(state):
    start = time.time()
    depth = 0
    if state[1] == 1:
        utility_value = max_value(state, depth)
    else:
        utility_value = min_value(state, depth)
    end = time.time()
    print("Time taken in seconds: ", end - start)
    return utility_value

#%% [markdown]
## Minimax Functions With Alpha Beta Pruning


#%%
def max_value_abp(state, alpha, beta, depth):
    # Check if one of four terminal states has been reached:
    terminal_state, utility_value = terminal_test(state)
    if not terminal_state:
        depth = depth + 1
        for next_state in successors(state, depth):
            v_ = min_value_abp(next_state, alpha, beta, depth)
            if v_ > utility_value:
                utility_value = v_
            if v_ >= beta:
                return utility_value
            if v_ > alpha:
                alpha = v_
    return utility_value

#%%
def min_value_abp(state, alpha, beta, depth):
    # Check if one of four terminal states has been reached:
    terminal_state, utility_value = terminal_test(state)
    if not terminal_state:
        depth = depth + 1
        for next_state in successors(state, depth):
            v_ = max_value_abp(next_state, alpha, beta, depth)
            if v_ < utility_value:
                utility_value = v_
            if v_ <= alpha:
                return utility_value
            if v_ < beta:
                beta = v_
    return utility_value

#%%
def minimax_value_abp(state):
    start = time.time()
    depth = 0
    alpha = 0
    beta = 0
    if state[1] == 1:
        utility_value = max_value_abp(state, alpha, beta, depth)
    else:
        utility_value = min_value_abp(state, alpha, beta, depth)
    end = time.time()
    print("Time taken in seconds: ", end - start)
    return utility_value


#%%
minimax_value_abp(([3, 1, 1], 1))
#%%
successors(([3,2],1), 1)

#%%
terminal_test(([1], 1))

#%%
max_value(([3,2], 1), 5)

#%%
min_value(([3,2], 2), 0)

#%%
minimax_value(([3, 2], 1))

#%%
minimax_value(([3, 2], 2))

#%%
minimax_value(([5, 4], 1))

#%%
minimax_value(([2, 2], 1))

#%%
minimax_value(([3, 3, 3], 1))

#%%
minimax_value_abp(([3, 3, 3], 1))

#%%
minimax_value_abp(([2,2], 1))

#%%
minimax_value(([2, 2, 2], 1))

#%%
minimax_value_abp(([2, 2, 2], 1))

#%%
minimax_value(([3, 1, 1], 1))

#%%
minimax_value_abp(([3, 3, 3, 3, 3, 3], 1))

