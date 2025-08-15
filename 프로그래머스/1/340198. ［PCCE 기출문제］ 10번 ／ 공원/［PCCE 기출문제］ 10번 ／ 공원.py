def solution(mats, park):
    m = len(park)
    n = len(park[0])
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    max_side = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if park[i-1][j-1] == "-1":   
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                max_side = max(max_side, dp[i][j])

    candidates = []
    for size in mats:
        if size <= max_side:
            candidates.append(size)

    if candidates:
        return max(candidates)
    else:
        return -1
