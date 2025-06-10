import sys

input = sys.stdin.readline

def dfs(start):
    visited[start] = True
    path.append(start)
    next_node = nums[start]

    if not visited[next_node]:
        dfs(next_node)
    elif next_node in path:
        idx = path.index(next_node)
        result.update(path[idx:])  # 사이클 구간만 추가


n = int(input())
nums = [0] + [int(input()) for _ in range(n)]
result = set()

for i in range(1, n + 1):
    visited = [False] * (n + 1)
    path = []
    dfs(i)

result = sorted(result)
print(len(result))
for i in result:
    print(i)
