import sys
input = sys.stdin.readline

R, C = map(int, input().split())
board = [list(input().strip()) for _ in range(R)]

dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1] 

def bfs():
    max_len = 0
    queue = set()
    queue.add((0, 0, board[0][0])) 

    while queue:
        x, y, path = queue.pop()
        max_len = max(max_len, len(path))
        if max_len == 26:
            return 26  # 최댓값이므로 즉시 반환

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < R and 0 <= ny < C:
                char = board[nx][ny]
                if char not in path:
                    queue.add((nx, ny, path + char))

    return max_len

print(bfs())
