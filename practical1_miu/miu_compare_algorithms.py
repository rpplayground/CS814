from miu_next_states import next_states
from miu_extend_path import extend_path
from miu_breadth_first_search import breadth_first_search
from miu_depth_limited_dfs import depth_limited_dfs
from miu_iterative_deepening import iterative_deepening
from miu_main import miu_search

def create_record(algorithm_name, goal, limit, goal_path, extend_path_counter, agenda_length, maximum_agenda_length, time_taken):
    algorithm_result = [{ "Algorithm" : algorithm_name, "Goal" : goal, "Limit" : limit, "Path" : goal_path,\
         "Path Length" : len(goal_path), "Extend Calls" : extend_path_counter, "Agenda Length" : agenda_length,\
              "Max Agenda Length" : maximum_agenda_length, "Time Taken" : time_taken}]
    return algorithm_result

def compare_algorithms(list_of_goals, limit):
    list_of_results = []
    for goal_state in list_of_goals:
        for model in ["breadth_first_search", "depth_limited_dfs", "iterative_deepening"]:
            # Run the model
            goal_path, extend_path_counter, agenda_length, maximum_agenda_length, time_taken = miu_search(goal_state, model, limit)
            # Gather the results
            list_of_results = list_of_results + create_record(model, goal_state, 0, goal_path, extend_path_counter, agenda_length, maximum_agenda_length, time_taken)
    return list_of_results
