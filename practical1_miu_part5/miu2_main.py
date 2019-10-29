import time
import pandas as pd
import numpy as np
from miu2_iterative_deepening import iterative_deepening

def run_search(goal):
    start_time = time.time()
    goal_path = iterative_deepening(goal)
    end_time = time.time()
    time_taken = end_time - start_time
    return goal_path, time_taken

def create_record(goal, goal_path, time_taken):
    algorithm_result = { "Goal" : goal, "Path" : goal_path, "Depth" : len(goal_path), "Time Taken" : time_taken }
    return algorithm_result

def iterate_through_goals(list_of_goals):
    results = []
    for goal in list_of_goals:
        goal_path, time_taken = run_search(goal)
        results.append(create_record(goal, goal_path, time_taken))
    results_dataframe = pd.DataFrame(results)
    return results_dataframe