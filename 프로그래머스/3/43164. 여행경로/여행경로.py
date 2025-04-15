import collections

def solution(tickets):
    graph = collections.defaultdict(list)
    
    for a, b in sorted(tickets, key=lambda x: x[1]):
        graph[a].append(b)
    
    route = []
    print(graph)

    def DFS(start):
        while graph[start]:
            DFS(graph[start].pop(0))
        route.append(start)
             

    DFS("ICN")
    return route[::-1]