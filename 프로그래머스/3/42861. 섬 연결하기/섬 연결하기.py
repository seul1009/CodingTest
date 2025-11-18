def find(parent, a):
    if parent[a] != a:
        parent[a] = find(parent, parent[a])
    return parent[a]

def union(parent, a, b):
    rootA = find(parent, a)
    rootB = find(parent, b)
    
    if rootA < rootB:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB
        
def solution(n, costs):
    answer = 0
    
    parent = [i for i in range(n)]
    costs.sort(key = lambda x : x[2])
    edge_count = 0
    
    for a, b, cost in costs:
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            answer += cost
            edge_count += 1
            
            if edge_count == n - 1:
                break
                
    return answer
                
            