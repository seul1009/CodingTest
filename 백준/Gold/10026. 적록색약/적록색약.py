import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input())
grid = [list(input().strip()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, color, board):
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if not visited[nx][ny] and board[nx][ny] == color:
                dfs(nx, ny, color, board)

# 적록색약이 아닌 사람
normal = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j, grid[i][j], grid)
            normal += 1

# 적록색약인 사람
for i in range(n):
    for j in range(n):
        if grid[i][j] == 'G':
            grid[i][j] = 'R'

visited = [[False] * n for _ in range(n)]
blindness = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j, grid[i][j], grid)
            blindness += 1

print(normal, blindness)