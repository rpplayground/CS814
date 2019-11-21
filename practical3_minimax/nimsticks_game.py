#%%
# Import stuff
from random import randrange
from minimax_nimsticks import *

#%%
# Helper function to print out game state:
def print_game_state(state, round):
    if state[1] == 1:
        player_name = "Human"
    else:
        player_name = "Computer"
    print("\n================================================================")
    print("Round {} - {} to play:".format(round, player_name))
    for pile_index, pile_size in enumerate(state[0]):
        print("\tPile {} - {} sticks".format(pile_index + 1, pile_size))

#%%
# Helper function to gather user input:
def get_user_input(min, max, prompt):
    while True:
        user_input = int(input(prompt))
        if user_input >= min and user_input <= max:
            break
        else:
            print("Please input an integer between {} and {}.".format(min, max))
    return user_input

# Prompt user for stuff to initiate the game
number_of_piles = get_user_input(1, 10, "Number of piles: ")
maximum_pile_size = get_user_input(1, 100, "Maximum number of sticks: ")
first_player = get_user_input(1, 2, "First player (enter either 1 for human, or 2 for computer): ")

# Initialise the game
initial_piles = []
for pile in range(0,number_of_piles):
    pile_size = randrange(1, maximum_pile_size)
    initial_piles.append(pile_size)
state = (initial_piles, first_player)

round = 1

# While game hasn't yet been won...
while True:
    # Print game state
    print_game_state(state, round)

    if state[1] == 1:
        piles = state[0]
        # It is the human player's turn - prompt them for their choice of pile and number of sticks:
        pile_to_pick_from = get_user_input(1, len(piles), "Pile to pick from (see above): ")
        pile_index = pile_to_pick_from - 1
        pile = piles[pile_index]
        if pile <= 3:
            max_pick = pile
        else:
            max_pick = 3
        pick = get_user_input(1, max_pick, "Number of sticks to remove (between 1 and {}): ".format(max_pick))
        # Calculate the next state accoridngly
        if pile >= pick:
            result = pile - pick
            if result != 0:
                new_piles = sorted(piles[:pile_index] + [result] + piles[pile_index + 1:])
            else:
                new_piles = sorted(piles[:pile_index] + piles[pile_index + 1:])
            state = (new_piles, 2)
            round = round + 1
    else:
        # Else, it is the computer's turn - calculate the successors
        list_of_successors = successors(state, 0)
        number_of_next_states = len(list_of_successors)
        for next_state_index, next_state in enumerate(list_of_successors):
            utility_value = minimax_value_abp(next_state)
            if utility_value == -1:
                # We've found a state that will allow the computer to win
                state = next_state
                print("Computer winning!")
                break
            elif next_state_index == number_of_next_states - 1:
                # We have reached the end of the list of successors so just select a random choice
                state = list_of_successors[randrange(0, number_of_next_states)]
                print("Computer losing!")
        
    # Check if we have reached the end of the game
    if state[0] == []:
        # Decide if the human or computer has won
        if state[1] == 1:
            winner = "Human"
        else:
            winner = "Computer"
        # Print the closing statement
        print("\n================================================================")
        print("Game over!  The {} wins!!!".format(winner))
        break

