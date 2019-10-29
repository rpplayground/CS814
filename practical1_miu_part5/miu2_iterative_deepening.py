from miu2_depth_limited_dfs import depth_limited_dfs

def iterative_deepening(goal):
    depth_limit = 2
    while True:
        goal_path = depth_limited_dfs(goal, depth_limit)
        if goal_path ==[]:
            depth_limit = depth_limit + 1
        else:
            break
    return goal_path