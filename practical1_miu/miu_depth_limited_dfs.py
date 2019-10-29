# University of Strathclyde - MSc Artificial Intelligence and Applications
# CS814 - Artificial Intelligence for Autonomous Systems
# Assignment 1 - Part 2 - MUI Next States Function
# File Created - 15th October 2019 - Barry Smart
# 
# ABOUT:
# This file contains the function that...

# We will use the next_states function, so let's import that:
from miu_extend_path import extend_path

def depth_limited_dfs(goal_string, limit, visited_list, extend_path_counter = 0, maximum_agenda_length = 0):
    # TODO - check that goal string contains only the letters M, I or U.
    # Initialise the agenda
    agenda = [["MI"]]
    goal_path = []
    # Check if the agenda has been primed with the goal!
    if agenda[0] == goal_string:
        goal_path = agenda[0]
        return goal_path, extend_path_counter, 0, maximum_agenda_length, visited_list
    while agenda != []:
        # Pop the first path from the agenda
        current_path = agenda.pop(0)
        path_length = len(current_path)
        # Track the maximum size that the agenda reaches
        agenda_length = len(agenda)
        if agenda_length > maximum_agenda_length:
            maximum_agenda_length = agenda_length
        if path_length <= limit:
            # Call the extend_path function
            new_paths, visited_list = extend_path(current_path, visited_list)
            # Increment the extend_paths counter by 1
            extend_path_counter = extend_path_counter + 1
            # Check last state from each path returned to see if we have found goal state
            for path in new_paths:
                if path[-1] == goal_string:
                    goal_path = path
                    break
                else:
                    # Then add these paths to the START of the agenda
                    agenda.insert(0, path)
        else:
            break
    return goal_path, extend_path_counter, agenda_length, maximum_agenda_length, visited_list