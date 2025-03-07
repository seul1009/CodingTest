import heapq

def dijkstra(start):
    distances = [float('inf')] * (N + 1)
    distances[start] = 0
    pq = []   
    heapq.heappush(pq, (0, start))  # heap에 가중치, 노드 삽입
    while pq:
        dist, now = heapq.heappop(pq)   
        if distances[now] >= dist:  
            for next_node, time in graph[now]:  
                if dist + time < distances[next_node]:  # 가중치가 더 작은 값이면 갱신
                    distances[next_node] = dist + time
                    heapq.heappush(pq, (dist + time, next_node))
    return distances

N, M, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, time = map(int, input().split())
    graph[a].append([b, time]) 

distances_from_X = dijkstra(X)  
distances_from_X[0] = 0

for i in range(1, N + 1):
    if i != X:
        reverse_distances = dijkstra(i) 
        distances_from_X[i] += reverse_distances[X] 

print(max(distances_from_X)) 
