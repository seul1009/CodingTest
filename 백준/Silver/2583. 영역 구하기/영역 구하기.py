import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

m, n, k = map(int, input().split())
field = [[0] * n for _ in range(m)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            field[y][x] = 1

def dfs(y, x):
    field[y][x] = 1
    size = 1

    for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ny, nx = y + dy, x + dx
        if 0 <= ny < m and 0 <= nx < n and field[ny][nx] == 0:
            size += dfs(ny, nx)
    return size

result = []
for y in range(m):
    for x in range(n):
        if field[y][x] == 0:
            result.append(dfs(y, x))

print(len(result))
print(*sorted(result))