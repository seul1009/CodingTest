def solution(n):
    result = []
    
    def hanoi(n, start, end, temp):
        if n == 1:
            result.append([start, end])
            return 
        hanoi(n-1, start, temp, end)
        result.append([start, end])
        hanoi(n-1, temp, end, start)
    hanoi(n, 1, 3, 2)  
    return result