from collections import deque

def bfs(start, wire_network, n):
    visited = [False for _ in range(n + 1)]
    q = deque([start])
    visited[start] = True
    count = 1
    
    while q:
        now = q.popleft()
        for nxt in wire_network[now]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)
                count += 1
                
    return count

def solution(n, wires):
    answer = float('inf')
    
    # 전선 끊음
    for w1, w2 in wires:
        temp_network = [[] for _ in range(n + 1)]
        
        for a, b in wires:
            if (a, b) == (w1, w2) or (a, b) == (w2, w1):
                continue
            temp_network[a].append(b)
            temp_network[b].append(a)
            
        count = bfs(1, temp_network, n)

        diff = abs(n - 2 * count)
        answer = min(answer, diff)

    return answer

