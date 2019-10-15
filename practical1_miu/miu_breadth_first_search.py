# University of Strathclyde - MSc Artificial Intelligence and Applications
# CS814 - Artificial Intelligence for Autonomous Systems
# Assignment 1 - Part 2 - MUI Next States Function
# File Created - 15th October 2019 - Barry Smart
# 
# ABOUT:
# This file contains the function that...

# We will use the next_states function, so let's import that:
from miu_extend_path import extend_path

def breadth_first_search(goal_string):
    # TODO - check that goal string contains only the letters M, I or U.
    # Initialise the agenda
    agenda = [["MI"]]
    # Initialise the counter for calls to next_states
    extend_path_counter = 0
    while True:
        # Pop the first path from the agenda
        current_path = agenda.pop(0)
        # Extract the last state from the current path
        last_state = current_path[-1]
        # Compare it with the goal state
        if last_state == goal_string:
            # If it is equal break from the while loop
            break
        else:
            # Else we need call the extend_path function
            new_paths = extend_path(current_path)
            # Then add these paths to the END of the agenda
            agenda = agenda + new_paths
            # Increment the extend_paths counter by 1
            extend_path_counter = extend_path_counter + 1
        
    print("Length of goal path:", len(current_path))
    print("Number of calls to extend_path:", extend_path_counter)
    print("Size of the agenda at point goal found:", len(agenda))
    # Return a list of paths.
    return current_path