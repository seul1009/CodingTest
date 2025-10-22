import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
K = int(input())
apples = [list(map(int, input().split())) for _ in range(K)]

L = int(input())
rotation = [list(input().split()) for _ in range(L)]

board = [[0] * N for _ in range(N)]

for a, b in apples:
    board[a-1][b-1] = 1

def bfs(start):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    direction = 0
    second = 0
    x, y = start
    q = deque([(x, y)])
    rot = 0

    while True:
        second += 1
        nx = x + dx[direction]
        ny = y + dy[direction]

        if nx < 0 or nx >= N or ny < 0 or ny >= N or (nx, ny) in q:
            return second

        if board[nx][ny] == 1:
            board[nx][ny] = 0
            q.append((nx, ny))
        else:
            q.append((nx, ny))
            q.popleft()

        x, y = nx, ny

        if rot < L and second == int(rotation[rot][0]):
            if rotation[rot][1] == 'L':
                direction = (direction - 1) % 4
            else:
                direction = (direction + 1) % 4
            rot += 1

print(bfs((0,0)))
