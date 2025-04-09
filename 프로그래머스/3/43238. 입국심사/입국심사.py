def solution(n, times):
    left, right = 1, max(times) * n
    
    while left <= right:
        mid = (left + right) // 2
        
        cnt = 0 # mid 시간 내에 심사 가능한 사람 수
        for time in times:
            cnt += mid // time
            
            if cnt >= n: 
                break
        
        if cnt >= n:
            right = mid - 1
            
        elif cnt < n:
            left = mid + 1
            
    return left