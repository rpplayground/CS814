from miu2_extend_path import extend_path

def depth_limited_dfs(goal, depth_limit, extend_count):
    agenda = [["MI"]]
    visited_list = {}
    while True:
        if agenda == []:
            return [], extend_count
        current_path = agenda.pop(0)
        current_path_end_state = current_path[-1]
        current_path_length = len(current_path)
        if current_path_length <= depth_limit:
            if (current_path_end_state not in visited_list) or (current_path_length < visited_list[current_path_end_state]):
                visited_list[current_path_end_state] = current_path_length
                new_paths = extend_path(current_path)
                extend_count = extend_count + 1
                for path in new_paths:
                    if path[-1] == goal:
                        return path, extend_count
                    else:
                        agenda = [path] + agenda