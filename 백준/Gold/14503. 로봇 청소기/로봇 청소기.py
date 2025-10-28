import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
# 처음 로봇청소기가 있는 좌표와 방향
r, c, d = map(int, input().split())

room = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

count = 0

# 큐에는 (r, c, d)
q = deque([(r, c, d)])

while q:
    x, y, d = q.popleft()

    # 현재 칸이 청소되지 않았으면 청소
    if room[x][y] == 0:
        room[x][y] = 2
        count += 1

    # 주변 4칸 중 청소되지 않은 칸 탐색
    moved = False
    nd = d
    for _ in range(4):
        nd = (nd + 3) % 4  # 반시계 방향 회전
        nx, ny = x + dx[nd], y + dy[nd]
        if 0 <= nx < N and 0 <= ny < M and room[nx][ny] == 0:
            q.append((nx, ny, nd))
            moved = True
            break

    # 청소되지 않은 칸이 없으면 후진
    if not moved:
        back_dir = (d + 2) % 4
        bx, by = x + dx[back_dir], y + dy[back_dir]
        if room[bx][by] != 1:  # 벽이 아니면 후진
            q.append((bx, by, d))
        else:  # 벽이면 중지
            break

print(count)