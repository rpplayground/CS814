from miu2_next_states import next_states

def extend_path(p):
    list_of_paths = []
    list_of_next_states = next_states(p[-1])
    for state in list_of_next_states:
        list_of_paths.append(p + [state])
    return list_of_paths