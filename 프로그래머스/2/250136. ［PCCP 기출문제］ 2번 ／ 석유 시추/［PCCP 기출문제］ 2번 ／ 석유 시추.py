from collections import deque

def solution(land):
    n, m = len(land), len(land[0])
    visited = [[False] * m for _ in range(n)] 
    col_oil = [0] * m
    
    
    def bfs(a, b):
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        
        queue = deque([(a, b)])
        visited[a][b] = True
        size = 0
        columns = set()
        
        while queue:
            x, y = queue.popleft()
            size += 1
            columns.add(y)

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and land[nx][ny] == 1:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
        
        for col in columns:
            col_oil[col] += size
    
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
    return max(col_oil)
        
    