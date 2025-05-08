from collections import deque
n, k = map(int, input().split())

visited = [0] * 100001

def bfs(start):
    q = deque()
    q.append(start)

    while q:
        now = q.popleft()

        if now == k:
            return visited[now]

        for next in [now - 1, now + 1, now * 2]:
            if 0 <= next <= 100000 and visited[next] == 0:
                visited[next] = visited[now] + 1
                q.append(next)
print(bfs(n))
