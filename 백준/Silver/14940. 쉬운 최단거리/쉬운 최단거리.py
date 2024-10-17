from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
distance = [[-1] * m for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(i, j):
    q = deque([(i, j)])
    distance[i][j] = 0

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = dx[d] + x, dy[d] + y

            if 0 <= nx < n and 0 <= ny < m and distance[nx][ny] == -1:
                if grid[nx][ny] == 1:
                    distance[nx][ny] = distance[x][y] + 1
                    q.append((nx, ny))
                elif grid[nx][ny] == 0:
                    distance[nx][ny] = 0

for i in range(n):
    for j in range(m):
        if grid[i][j] == 2:
            bfs(i, j)

for i in range(n):
    for j in range(m):
        if grid[i][j] == 0:
            print(0, end=' ')
        else:
            print(distance[i][j], end=' ')
    print()