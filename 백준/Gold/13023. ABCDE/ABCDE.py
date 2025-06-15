import sys

input = sys.stdin.readline

def dfs(node, depth):
    global found
    if found:  
        return
    if depth == 5:
        found = True
        return
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor, depth + 1)
    visited[node] = False  

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
found = False
visited = [False] * n

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n):
    dfs(i, 1)
    if found:
        break

print(1 if found else 0)
