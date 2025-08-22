import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
Map = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[[False] * 2 for _ in range(m)] for __ in range(n)]

queue = deque([(0, 0, 0, 1)])
visited[0][0][0] = True

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

ans = -1

while queue:
    x, y, broken, dist = queue.popleft()

    if x == n - 1 and y == m - 1:
        ans = dist
        break
        
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if Map[nx][ny] == 0 and not visited[nx][ny][broken]:
                visited[nx][ny][broken] = True
                queue.append((nx, ny, broken, dist+1))

            elif Map[nx][ny] == 1 and broken == 0 and not visited[nx][ny][broken]:
                visited[nx][ny][broken] = True
                queue.append((nx, ny, 1, dist+1))

print(ans)