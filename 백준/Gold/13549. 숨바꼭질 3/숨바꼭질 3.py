from collections import deque

def solution(N, K):
    MAX = 100000
    dist = [-1] * (MAX + 1)
    dq = deque()
    
    dq.append(N)
    dist[N] = 0
    
    while dq:
        x = dq.popleft()

        if x == K:
            return dist[x]

        # 1) 순간이동 (비용 0)
        nx = x * 2
        if 0 <= nx <= MAX and dist[nx] == -1:
            dist[nx] = dist[x]
            dq.appendleft(nx)

        # 2) 걷기 -1, +1 (비용 1)
        for nx in (x - 1, x + 1):
            if 0 <= nx <= MAX and dist[nx] == -1:
                dist[nx] = dist[x] + 1
                dq.append(nx)

# 입력
N, K = map(int, input().split())
print(solution(N, K))
