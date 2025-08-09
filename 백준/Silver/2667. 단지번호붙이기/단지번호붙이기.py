import sys
input = sys.stdin.readline

n = int(input())
smap = [list(input()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(x, y):
    visited[x][y] = True
    count = 1

    for dx, dy in dirs:
        nx, ny = x + dx, y + dy

        if 0 <= nx < n and 0 <= ny < n:
            if not visited[nx][ny] and smap[nx][ny] == '1':
                count += dfs(nx, ny)
    return count

sizes = []
for i in range(n):
    for j in range(n):
        if smap[i][j] == '1' and not visited[i][j]:
            sizes.append(dfs(i, j))

sizes.sort()
print(len(sizes))
for i in sizes:
    print(i)