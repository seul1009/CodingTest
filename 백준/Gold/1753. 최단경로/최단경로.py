import heapq
import sys
input = sys.stdin.readline

def dijkstra(start, graph):
    queue = []
    distances = { node : float('inf') for node in graph }
    distances[start] = 0
    heapq.heappush(queue, [distances[start], start])

    while queue:
        now_dist, now = heapq.heappop(queue)

        if distances[now] < now_dist:
            continue

        for new, new_dist in graph[now]:
            distance = now_dist + new_dist
            if distance < distances[new]:
                distances[new] = distance
                heapq.heappush(queue, [distance, new])

    return distances

V, E = map(int, input().split())
start = int(input())

graph = {i:[] for i in range(1, V + 1)}

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

distances = dijkstra(start, graph)

for i in range(1, V+1):
    if distances[i] != float('inf'):
        print(distances[i])
    else:
        print("INF")



