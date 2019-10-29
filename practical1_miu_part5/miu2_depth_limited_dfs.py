from miu2_extend_path import extend_path

def depth_limited_dfs(goal, depth_limit):
    agenda = [["MI"]]
    visited_list = []
    goal_path = []
    while agenda != []:
        next_path = agenda.pop(0)
        path_length = len(next_path)
        if path_length <= depth_limit:
            new_paths, visited_list = extend_path(next_path, visited_list)
            for path in new_paths:
                if path[-1] == goal:
                    goal_path = path
                    break
                else:
                    agenda.insert(0, path)
    return goal_path