import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y, h):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque()
    q.append([x, y])
    visited[x][y] = True

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and region[nx][ny] > h and visited[nx][ny] == False:
                visited[nx][ny] = True
                q.append([nx, ny])

n = int(input())
max_list = [] # 안전 영역 최대 개수
max_num = 0
region = []

for _ in range(n):
    region.append(list(map(int, input().split())))

for i in region:
    for j in i:
        if max_num < j:
            max_num = j

max_height = max(map(max, region))


for h in range(max_height + 1):
    visited = [[False] * n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if region[i][j] > h and visited[i][j] == False:
                bfs(i, j, h)
                count += 1
    max_list.append(count)

print(max(max_list))
