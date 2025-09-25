n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * n for _ in range(n)]
def dfs(x, y):
    if x == n-1 and y == n-1:
        return 1

    if dp[x][y] != -1:
        return dp[x][y]

    jump = graph[x][y]
    if jump == 0:
        return 0

    dp[x][y] = 0

    if x + jump < n:
        dp[x][y] += dfs(x + jump, y)

    if y + jump < n:
        dp[x][y] += dfs(x, y + jump)

    return dp[x][y]

print(dfs(0, 0))