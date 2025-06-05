import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
routes = [list(map(int, input().split())) for _ in range(n)]
result = [[0] * n for _ in range(n)]

def bfs(start):
    visited = [False] * n
    queue = deque([start])

    while(queue):
        now = queue.popleft()
        for next in range(n):     
            if not visited[next] and routes[now][next] == 1:
                visited[next] = True
                queue.append(next)
                result[start][next] = 1

for i in range(n):
    bfs(i)

for r in result:
    print(' '.join(map(str, r)))
