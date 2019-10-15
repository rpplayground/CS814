# University of Strathclyde - MSc Artificial Intelligence and Applications
# CS814 - Artificial Intelligence for Autonomous Systems
# Assignment 1 - Part 2 - MUI Next States Function
# File Created - 15th October 2019 - Barry Smart
# 
# ABOUT:
# This file contains the function that, when passed a current path p, computes next possible paths based on what is returned by the next_states function.
# The function returns a list of possible next paths.

# We will use the next_states function, so let's import that:
from miu_next_states import next_states

def extend_path(p):
    # TODO - check p is a single level list containing states that are constructed only of the letters M, I or U.
    # Create an empty list into which we will build the list of lists that will be returned by the function
    list_of_all_possible_paths = []
    # Pick the last state s form the path.
    intermediate_state = p[-1]
    # Compute next states from that element:
    list_of_next_states = next_states(intermediate_state)
    # Iterate through each state returned
    for state in list_of_next_states:
        # Create new paths for each of the next states.
        extended_path = p.copy()
        extended_path.append(state)
        list_of_all_possible_paths = list_of_all_possible_paths + [extended_path]
    # Return a list of paths.
    return list_of_all_possible_paths
