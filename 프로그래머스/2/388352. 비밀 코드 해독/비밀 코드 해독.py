from itertools import combinations

def solution(n, q, ans):
    count = 0
    num = list(range(1, n + 1))
    correct = list(combinations(num, 5))
    
    for cor in correct:
        is_correct = True
        for code, answer in zip(q, ans):
            if len(set(cor) & set(code)) != answer:
                is_correct = False
                break
        if is_correct:
            count += 1
    return count
        
    