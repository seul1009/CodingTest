def solution(ability):
    n = len(ability)  # 학생 수
    m = len(ability[0])  # 종목 수
    visited = [False] * n
    max_score = 0

    def dfs(idx, score):
        global max_score
        if idx == m:
            max_score = max(max_score, score)
            return

        for i in range(n):
            if not visited[i]:
                visited[i] = True
                dfs(idx + 1, score + ability[i][idx])
                visited[i] = False  # 백트래킹

    dfs(0, 0)
    return max_score
