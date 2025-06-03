import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]
temp = [[0] * m for i in range(n)] # 복사용

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0

# 바이러스 확산
def virus(x, y):
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)

# 안전영역 개수
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

# 벽 3개 세우기, 안전영역 계산
def dfs(count):
    global result
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = lab[i][j]

        # 모든 바이러스 위치에서 확산
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)

        # 안전영역 계산
        result = max(result, get_score())
        return

    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0:
                lab[i][j] = 1
                dfs(count + 1)
                lab[i][j] = 0  # 백트래킹 (벽 제거)
dfs(0)
print(result)