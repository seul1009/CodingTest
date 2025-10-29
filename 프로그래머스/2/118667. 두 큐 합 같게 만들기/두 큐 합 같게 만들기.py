from collections import deque

def solution(queue1, queue2):
    q1, q2 = deque(queue1), deque(queue2)
    sum1, sum2 = sum(q1), sum(q2)
    total = sum1 + sum2
    
    if total % 2 !=0:
        return -1
    
    target = total // 2
    count = 0
    limit = len(q1) * 3
    
    while count < limit:
        if sum1 == target:
            return count
        
        if sum1 > target:
            x = q1.popleft()
            q2.append(x)
            sum1 -= x
            sum2 += x
        else:
            x = q2.popleft()
            q1.append(x)
            sum2 -= x
            sum1 += x
        count += 1
    
    return -1

