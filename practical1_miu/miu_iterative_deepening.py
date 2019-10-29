# University of Strathclyde - MSc Artificial Intelligence and Applications
# CS814 - Artificial Intelligence for Autonomous Systems
# Assignment 1 - Part 2 - MUI Next States Function
# File Created - 15th October 2019 - Barry Smart
# 
# ABOUT:
# This file contains the function that...

# We will use the next_states function, so let's import that:
from miu_depth_limited_dfs import depth_limited_dfs

def iterative_deepening(goal_string):
    # TODO - check that goal string contains only the letters M, I or U.
    # Initialise depth limit
    extend_path_counter = 0
    maximum_agenda_length = 0
    depth_limit = 1
    visited_list = []
    while True:
        goal_path, extend_path_counter, agenda_length, maximum_agenda_length, visited_list = \
            depth_limited_dfs(goal_string, depth_limit, visited_list, extend_path_counter, maximum_agenda_length)
        if goal_path == []:
            depth_limit = depth_limit + 1
        else:
            break     
    return goal_path, extend_path_counter, agenda_length, maximum_agenda_length