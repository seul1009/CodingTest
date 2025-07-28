import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = True

    while queue:
        now = queue.popleft()
        for next in range(n):
            if graph[now][next] == 1 and not visited[next]:
                visited[next] = True
                queue.append(next)

n = int(input())
m = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

plan = list(map(int, input().split()))

visited = [False] * n
bfs(plan[0] - 1)

result = True
for city in plan:
    if not visited[city - 1]:
        result = False
        break
print("YES" if result else "NO")
