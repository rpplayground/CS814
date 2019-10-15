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
    depth_limit = 1
    while True:
        goal_path = depth_limited_dfs(goal_string, depth_limit)
        if goal_path == []:
            depth_limit = depth_limit + 1
        else:
            break     
    return goal_path