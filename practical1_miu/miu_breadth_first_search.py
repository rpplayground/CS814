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
    # Initialise the agenda and visited list
    agenda = [["MI"]]
    visited_list = []
    # Initialise the counter for calls to next_states
    extend_path_counter = 0
    # Maximum agenda size
    maximum_agenda_length = 0
    while True:
        # Pop the first path from the agenda
        current_path = agenda.pop(0)
        # Track the maximum length of agenda encountered
        agenda_length = len(agenda)
        if agenda_length > maximum_agenda_length:
            maximum_agenda_length = agenda_length
        # Extract the last state from the current path
        last_state = current_path[-1]
        # Compare it with the goal state
        if last_state == goal_string:
            # If it is equal break from the while loop
            break
        else:
            # Else we need call the extend_path function
            new_paths, visited_list = extend_path(current_path, visited_list)
            # Then add these paths to the END of the agenda
            agenda = agenda + new_paths
            # Increment the extend_paths counter by 1
            extend_path_counter = extend_path_counter + 1
    goal_path = current_path        
    return goal_path, extend_path_counter, agenda_length, maximum_agenda_length