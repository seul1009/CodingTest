import sys
import heapq
input = sys.stdin.readline

n = int(input())
m = int(input())
INF = int(1e9)

distance = [INF] * (n + 1)
bus = [[] for _ in range(n + 1)]

for i in range(m):
    d, a, c = map(int, input().split())
    bus[d].append((a, c))

def dijkstra(s):
    q = []
    heapq.heappush(q, (0, s))
    distance[s] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in bus[now]: # 현재 노드와 연결된 다른 노드 확인
            cost = dist + i[1] # 현재 노드를 거쳐 가는 비용 계산
            if cost < distance[i[0]]: # 계산된 비용이 현재 기록된 최단 거리보다 짧으면 갱신
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

s, e = map(int, input().split())
dijkstra(s)
print(distance[e])
