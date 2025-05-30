from collections import deque
import sys

input = sys.stdin.readline
n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def DFS(start):
    visited[start] = True
    print(start, end = " ")
    for g in graph[start]:
        if not visited[g]:
            DFS(g)

def BFS(start):
    queue = deque([start])
    visited[start] = True
    while queue:
        p = queue.popleft()
        print(p, end = " ")
        for g in graph[p]:
            if not visited[g]:
                visited[g] = True
                queue.append(g)

for i in graph:
    i.sort()

visited = [False] * (n + 1)

DFS(v)
print()

visited = [False] * (n + 1)
BFS(v)