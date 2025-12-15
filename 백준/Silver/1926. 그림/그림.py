import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    cnt = 1
    q = deque([start])

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and paper[nx][ny] == 1:
                    visited[nx][ny] = True
                    q.append([nx, ny])
                    cnt += 1
    return cnt

n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
result = []

cnt_picture = 0
max_size = 0

for i in range(n):
    for j in range(m):
        if paper[i][j] == 1 and not visited[i][j]:
            visited[i][j] = True
            size = bfs((i, j))
            cnt_picture += 1
            max_size = max(max_size, size)

print(cnt_picture, max_size)



