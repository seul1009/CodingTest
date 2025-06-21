def solution(wallet, bill):
    answer = 0
    w1, w2 = wallet
    b1, b2 = bill
    
    while True:
        if (b1 <= w1 and b2 <= w2) or (b1 <= w2 and b2 <= w1):
            break
            
        if b1 > b2:
            b1 //= 2
        else:
            b2 //= 2
        answer += 1
        
    return answer
            