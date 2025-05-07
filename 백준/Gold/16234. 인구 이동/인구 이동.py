from collections import deque
n, l, r = map(int, input().split())
country = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, visited):
    q = deque()
    q.append((x, y))
    union = [(x, y)]
    total = country[x][y]
    visited[x][y] = 1

    while q:
        a, b = q.popleft()
        for i in range(4):
            nx, ny = a + dx[i], b + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if l <= abs(country[a][b] - country[nx][ny]) <= r :
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                    union.append((nx, ny))
                    total += country[nx][ny]

    if len(union) > 1:
        avg = total // len(union)
        for x, y in union:
            country[x][y] = avg
        return True
    return False

days = 0
while True:
    visited = [[0] * n for _ in range(n)]
    moved = False

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                if bfs(i, j, visited):
                    moved = True

    if not moved:
        break
    days += 1

print(days)




