def solution(s):
    count=0
    count_zero=0
    while s!="1":
        count+=1
        count_zero+=s.count('0')
        s=s.replace('0','')
        c=len(s)
        s=bin(c)[2:]

    return [count, count_zero]
    
    