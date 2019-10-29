import time
from miu_breadth_first_search import breadth_first_search
from miu_depth_limited_dfs import depth_limited_dfs
from miu_iterative_deepening import iterative_deepening

def miu_search(goal_state, method, limit):
    start_time = time.time()
    if method == "breadth_first_search":
        goal_path, extend_path_counter, agenda_length, maximum_agenda_length = breadth_first_search(goal_state)
    elif method == "depth_limited_dfs":
        goal_path, extend_path_counter, agenda_length, maximum_agenda_length = depth_limited_dfs(goal_state, limit)
    elif method == "iterative_deepening":
        goal_path, extend_path_counter, agenda_length, maximum_agenda_length = iterative_deepening(goal_state)
    else:
        return
    end_time = time.time()
    time_taken = end_time - start_time
    print("Run mode {} for string {} in time {}".format(method, goal_state, time_taken))
    return goal_path, extend_path_counter, agenda_length, maximum_agenda_length, time_taken


