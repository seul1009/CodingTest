import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
visited = [[-1] * n for _ in range(m)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def solution(x, y):
    if x == m-1 and y == n-1:
        return 1

    if visited[x][y] != -1:
        return visited[x][y]

    visited[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < m and 0 <= ny < n and arr[nx][ny] < arr[x][y]:
            visited[x][y] += solution(nx, ny)
    return visited[x][y]

print(solution(0, 0))