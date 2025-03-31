from collections import deque
def solution(n, edge):
    graph = [[] for _ in range(n + 1)]
    visited = [0] * (n + 1)
    
    for (a, b) in edge:
        graph[a].append(b)
        graph[b].append(a)
        
    q = deque()
    q.append(1)
    visited[1] = 1
    
    while q:
        s = q.popleft()
        
        for i in graph[s]:
            if not visited[i]:
                visited[i] = visited[s] + 1
                q.append(i)
    result = max(visited)
    return visited.count(result)
                
            
        
        
        