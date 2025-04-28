def solution(k, m, score):
    result=0
    score.sort(reverse=True)
    score=score[:len(score)-(len(score)%m)]
    for i in range(0, len(score), m):
        result+=min(score[i:i+m])
    return result*m
        