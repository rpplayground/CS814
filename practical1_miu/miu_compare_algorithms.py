from miu_next_states import next_states
from miu_extend_path import extend_path
from miu_breadth_first_search import breadth_first_search
from miu_depth_limited_dfs import depth_limited_dfs
from miu_iterative_deepening import iterative_deepening

def create_record(algorithm_name, goal, limit, goal_path, extend_path_counter, agenda_length, maximum_agenda_length):
    algorithm_result = [{ "Algorithm" : algorithm_name, "Goal" : goal, "Limit" : limit, "Path" : goal_path, "Path Length" : len(goal_path), "Extend Calls" : extend_path_counter, "Agenda Length" : agenda_length, "Max Agenda Length" : maximum_agenda_length }]
    return algorithm_result

def compare_algorithms(list_of_goals, limit):
    list_of_results = []
    for goal_state in list_of_goals:
        # Run each of the models
        # Breadth First Search
        goal_path, extend_path_counter, agenda_length, maximum_agenda_length = breadth_first_search(goal_state)
        list_of_results = list_of_results + create_record("Breadth First Search", goal_state, 0, goal_path, extend_path_counter, agenda_length, maximum_agenda_length)
        # Depth Limited Depth First Search
        goal_path, extend_path_counter, agenda_length, maximum_agenda_length = depth_limited_dfs(goal_state, limit)
        list_of_results = list_of_results + create_record("Depth Limited Depth First Search", goal_state, limit, goal_path, extend_path_counter, agenda_length, maximum_agenda_length)
        # Iterative Deepening
        goal_path, extend_path_counter, agenda_length, maximum_agenda_length = iterative_deepening(goal_state)
        list_of_results = list_of_results + create_record("Iterative Deepening", goal_state, limit, goal_path, extend_path_counter, agenda_length, maximum_agenda_length)
    return list_of_results
