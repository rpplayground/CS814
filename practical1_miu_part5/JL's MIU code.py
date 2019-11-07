import time

def JL_next_states(s):
    results = []
    if s[-1] == 'I':
        results.append(s + 'U')
    if s[0] == 'M':
        results.append(s + s[1:])
    for i in range(len(s)-2):
        if s[i:i+3] == 'III':
            results.append(s[0:i] + 'U' + s[i+3:])
    for i in range(len(s)-1):
        if s[i:i+2] == 'UU':
            results.append(s[0:i] + s[i+2:])
    return JL_remove_duplicates(results)

def JL_remove_duplicates(l):
    res = []
    for x in l:
        if x not in res:
            res.append(x)
    return res

def JL_extend_path(p):
    results = []
    ns = JL_next_states(p[-1])
    for s in ns:
        results.append(p + [s])
    return results

def JL_breadth_first_search(goal_state):
    extend_count = 0
    agenda = [['MI']]
    while agenda != []:
        cp = agenda[0]
        agenda = agenda[1:]
        if cp[-1] == goal_state:
            print('Solution length =', len(cp))
            print('Calls to extend_path =', extend_count)
            print('Length of the agenda =', len(agenda))
            return cp
        else:
            agenda = agenda + JL_extend_path(cp)
            extend_count += 1

def JL_bfs(s):
    return JL_breadth_first_search(s)

def JL_depth_limited_dfs(goal_state, limit, extend_count):
    agenda = [['MI']]
    while True:
        if agenda == []:
            return [], extend_count, 0
        cp = agenda[0]
        agenda = agenda[1:]
        if cp[-1] == goal_state:
            return cp, extend_count, len(agenda)
        if len(cp) < limit:
            agenda = JL_extend_path(cp) + agenda
            extend_count += 1

def JL_iterative_deepening(goal_state):
    limit = 1
    extend_count = 0
    while True:
        res = JL_depth_limited_dfs(goal_state, limit, extend_count)
        if res[0] != []:
            print('Solution length =', len(res[0]))
            print('Calls to extend_path =', res[1])
            print('Length of the agenda =', res[2])
            return res[0]
        else:
            limit += 1
            extend_count = extend_count + res[1]

def JL_ids(goal_state):
    return JL_iterative_deepening(goal_state)

def JL_explore_levels():
    states = ['MI']
    level = 1
    total_states = 1
    while True:
        print('At level', level, 'there are', len(states), 'states,',
              'so', total_states, 'in total.')
        new_states = []
        for s in states:
            new_states = new_states + JL_next_states(s)
        states = new_states
        total_states = total_states + len(new_states)
        level += 1
        
def JL_next_string(string):
    result = ''
    carry = 1
    for i in range(len(string) - 1, -1, -1):
        if carry == 0:
            result = string[i] + result
        if string[i] == 'I' and carry == 1:
            result = 'U' + result
            carry = 0
        if string[i] == 'U' and carry == 1:
            result = 'I' + result
        if string[i] == 'M' and carry == 1:
            result = 'MI' + result
    return result

def JL_test_all():
    string = 'MI'
    while True:
        if JL_i_count(string) % 3 == 0:
            pass
        elif string in ['MIUUUI', 'MUIUUI', 'MUUIUI', 'MUUUII']: # too hard
            print(string, 'is beyond my capabilties (at the moment)')
            pass
        else:
            print('Goal string: {}'.format(string))
            start = time.time()
            print(JL_iterative_deepening(string))
            end = time.time()
            print('Time taken:', end - start)            
        string = JL_next_string(string)

def JL_i_count(string):
    count = 0
    for c in string:
        if c == 'M':
            count += 0
        if c == 'I':
            count += 1
        if c == 'U':
            count += 3
    return count
        
def JL_main():
    print('Welcome to the MIU string searching program.')
    print('Type a string to search for or Q to quit.')
    print('If your search takes too long, hit ctrl-c to exit.')
    while True:
        goal = input('String to search for: ')
        if goal == 'q' or goal == 'Q':
            return
        start = time.time()
        print(JL_iterative_deepening(goal))
        end = time.time()
        print('Time taken:', end - start)

def JL_test(goal):
    start = time.time()
    search_result = JL_iterative_deepening(goal)
    end = time.time()
    print('Time taken:', end - start)
    return search_result
