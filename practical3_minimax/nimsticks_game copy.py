#%%
# Import stuff
from random import randrange

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

# Set up infinite loop until game has been won by either computer or the human...
while True:
    # Print game state - number of sticks left in each pile...

    # IF it is the player's turn:
        # First - ask which pile they want to pick from
        # Note : you will need to caculate number_of_piles, this will reduce as the game is played...
        pile_to_pick_from = get_user_input(1, number_of_piles, "Pile to pick from (see above): ")
        # Second - ask how many sticks they want to pick:
        # Note : you will need to determine maximum_possible_pick which is dependent on how many sticks are left in the chosen pile and will be between 1 and 3...
        pick = get_user_input(1, maximum_possible_pick, "Number of sticks to remove (between 1 and {}): ".format(max_pick))
        # Third - calculate the next state accoridngly by removing the sticks from the pile - note if the pile goes to 0 you will need to remove it altogether
    # ELSE it is the computer's turn:
        # Calculate all of the successors from the current state
        # For each successor:
            # Calculate the utility value (call minimax_value_with_alphabeta_pruning on it!)
            # IF a state is found where the computer will win, pick that and break from the FOR loop
            # ELSE if we reach the end and no state has been found where the computer will win, pick one at random and return that (hoping the human will make a mistake!)
        
    # IF we have reached the end of the game
        # Decide if the human or computer has won
        # IF human wins:
            winner = "Human"
        # ELSE
            winner = "Computer"
        # Print the closing statement
        print("\n================================================================")
        print("Game over!  The {} wins!!!".format(winner))
        break

