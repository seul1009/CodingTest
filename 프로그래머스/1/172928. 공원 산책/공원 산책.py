def solution(park, routes):
    direction = {'N': [-1, 0], 'S': [1, 0], 'W': [0, -1], 'E': [0, 1]}
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == "S":
                x, y = i, j
                break
    
    for route in routes:
        d, n = route.split()
        dx, dy = x, y
        
        for _ in range(int(n)):
            nx = x + direction[d][0]
            ny = y + direction[d][1]
            
            if 0 <= nx < len(park) and 0 <= ny < len(park[0]) and park[nx][ny] != "X":
                x, y = nx, ny
            else:
                x, y = dx, dy
                break
    return [x, y]
    