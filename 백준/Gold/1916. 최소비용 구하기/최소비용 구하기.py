import sys
import heapq
input = sys.stdin.readline

N = int(input())
M = int(input())
INF = int(1e9)

distance = [INF] * (N+1)
bus = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, dist = map(int, input().split())
    bus[a].append((b, dist))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for nxt, cost in bus[now]:  # nxt: 다음 노드, cost: 가중치
            new_cost = dist + cost
            if new_cost < distance[nxt]:
                distance[nxt] = new_cost
                heapq.heappush(q, (new_cost, nxt))

start, end = map(int, input().split())
dijkstra(start)
print(distance[end])



