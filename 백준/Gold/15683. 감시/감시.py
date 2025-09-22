import sys
input = sys.stdin.readline

n, m = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cctv_type = {
    1: [[0], [1], [2], [3]],                # 상, 하, 좌, 우
    2: [[0, 1], [2, 3]],                    # 상+하, 좌+우
    3: [[0, 3], [3, 1], [1, 2], [2, 0]],    # 상+우, 우+하, 하+좌, 좌+상
    4: [[1, 2, 3], [0, 2, 3], [0, 1, 3], [0, 1, 2]], 
    5: [[0, 1, 2, 3]]                        
}

cctvs = []
for i in range(n):
    for j in range(m):
        if 1 <= Map[i][j] <= 5:
            cctvs.append((i, j, Map[i][j]))

min_blind = 1e9

def watch(board, x, y, dirs):
    for d in dirs:
        nx, ny = x, y
        while True:
            nx += dx[d]
            ny += dy[d]
            if not (0 <= nx < n and 0 <= ny < m):
                break
            if board[nx][ny] == 6:
                break
            if board[nx][ny] == 0:
                board[nx][ny] = '#'

def dfs(depth, Map):
    global min_blind
    if depth == len(cctvs):
        cnt = sum(row.count(0) for row in Map)
        min_blind = min(min_blind, cnt)
        return

    x, y, ctype = cctvs[depth]
    for dirs in cctv_type[ctype]:
        temp = [row[:] for row in Map]
        watch(temp, x, y, dirs)
        dfs(depth + 1, temp)

dfs(0, Map)
print(min_blind)
