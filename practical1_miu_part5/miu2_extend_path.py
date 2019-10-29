from miu2_next_states import next_states

def extend_path(p, visited_list):
    list_of_paths = []
    list_of_next_states = next_states(p[-1])
    for state in list_of_next_states:
        if state not in visited_list:
            visited_list.append(state)
            p_copy = p.copy()
            p_copy.append(state)
            list_of_paths.append(p_copy)
    return list_of_paths, visited_list