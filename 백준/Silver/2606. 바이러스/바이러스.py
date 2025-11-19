import sys
input = sys.stdin.readline

def dfs(start):
    global cnt
    visited[start] = 1
    for nxt in nodes[start]:
        if not visited[nxt]:
            cnt += 1
            dfs(nxt)


n = int(input())
edge = int(input())
nodes = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
cnt = 0

for _ in range(edge):
    a, b = map(int, input().split())
    nodes[a].append(b)
    nodes[b].append(a)

dfs(1)
print(cnt)

