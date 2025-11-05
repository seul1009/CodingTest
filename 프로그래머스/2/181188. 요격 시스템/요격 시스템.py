def solution(targets):
    shoot = -1
    count = 0
    
    targets.sort(key = lambda x: x[1])
    
    for s, e in targets:
        if s >= shoot:
            shoot = e
            count += 1
    return count
        