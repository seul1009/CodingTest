def solution(word):
    vowels = ['A', 'E', 'I', 'O', 'U']
    words = []
    
    def dfs(current):
        if current:  # 빈 문자열 제외
            words.append(current)
        if len(current) == 5:  # 최대 길이 5
            return
        
        for v in vowels:
            dfs(current + v)
    
    dfs("")  # 시작
    return words.index(word) + 1
