import sys
from collections import deque
input = sys.stdin.readline
m, n = map(int, input().split())
tomato = []
queue = deque()

dx = [-1, 1, 0 ,0]
dy = [0, 0, -1, 1]

for _ in range(n):
    tomato.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            queue.append([i, j])
def BFS():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < m and tomato[nx][ny] == 0:
                tomato[nx][ny] = tomato[x][y] + 1
                queue.append((nx, ny))

BFS()

day = 0
for row in tomato:
    for i in row:
        if i == 0:
            print(-1)
            exit() # 0인 값이 있으면 익지 않은 토마토가 있는 것이므로 -1을 출력하고 종료
    else:
        day = max(day, max(row))
print(day - 1) # 토마토에 1부터 +1 했으므로 최소 일수는 -1 해주어야 함

