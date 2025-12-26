def solution(s, skip, index):
    answer = ''
    alp = 'abcdefghijklmnopqrstuvwxyz'
    
    for sk in skip:
        alp = alp.replace(sk, '')
    
    for a in s:
        idx = (alp.index(a) + index ) % len(alp)
        answer += alp[idx]
    
    return answer