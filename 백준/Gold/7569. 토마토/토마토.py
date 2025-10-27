import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int, input().split())
boxes = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

def bfs():
    q = deque()

    for tomato in tomatoes:
        q.append(tomato)

    dz = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, 1, -1, 0, 0]
    dx = [0, 0, 0, 0, 1, -1]

    while q:
        z, y, x = q.popleft()

        for i in range(6):
            nz, ny, nx = z + dz[i], y + dy[i], x + dx[i]

            if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H and boxes[nz][ny][nx] == 0:
                boxes[nz][ny][nx] = boxes[z][y][x] + 1
                q.append((nz, ny, nx))

tomatoes = []
for h in range(H):
    for n in range(N):
        for m in range(M):
            if boxes[h][n][m] == 1:
                tomatoes.append((h, n, m))
bfs()

result = 0
for h in range(H):
    for n in range(N):
        for m in range(M):
            if boxes[h][n][m] == 0:
                print(-1)
                exit(0)
            result = max(result, boxes[h][n][m])
print(result - 1)