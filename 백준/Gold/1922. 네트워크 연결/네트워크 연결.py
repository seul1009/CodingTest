import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x_root = find(x)
    y_root = find(y)
    if x_root != y_root:
        parent[y_root] = x_root
        return True
    return False

N, M = int(input()), int(input())
graph = []
for _ in range(M):
    a, b, c = map(int, input().split())
    graph.append((c, a, b))

graph.sort()
parent = [i for i in range(N + 1)]

total_cost = 0


for c, a, b in graph:
    if union(a, b):
        total_cost += c

print(total_cost)


