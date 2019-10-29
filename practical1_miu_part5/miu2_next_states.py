def next_states(s):
    results = []
    if s[-1] == 'I':
        results.append(s + 'U')
    # This if statement can removed as "rule 2" always applies
    # if s[0] == 'M':
    results.append(s + s[1:])
    for i in range(len(s)-2):
        if s[i:i+3] == 'III':
            results.append(s[0:i] + 'U' + s[i+3:])
    for i in range(len(s)-1):
        if s[i:i+2] == 'UU':
            results.append(s[0:i] + s[i+2:])
    return remove_duplicates(results)

def remove_duplicates(l):
    res = []
    for x in l:
        if x not in res:
            res.append(x)
    return res