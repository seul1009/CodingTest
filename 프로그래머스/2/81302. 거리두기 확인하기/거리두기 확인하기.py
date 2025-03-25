from collections import deque
def manhattan(place):
    direction = [(-1,0), (1,0), (0,-1), (0,1)]
    dict = []
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                q = deque([(i, j, 0)])
                visited = set()
                visited.add((i, j))
                
                while q:
                    x, y, dist = q.popleft()
                    if dist >= 2:
                        continue
                    
                    for dx, dy in direction:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < 5 and 0 <= ny < 5 and (nx, ny) not in visited:
                            if place[nx][ny] == 'P':
                                return 0
                            
                            if place[nx][ny] == 'O':
                                q.append((nx, ny, dist + 1))
                            visited.add((nx, ny))
    return 1
                            
def solution(places):
    return [manhattan(place) for place in places]