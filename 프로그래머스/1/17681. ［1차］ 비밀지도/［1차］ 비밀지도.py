def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        string = ""
        num = arr1[i] | arr2[i]

        for _ in range(n):
            if num % 2 == 0:
                string = ' ' + string
            else:
                string = '#' + string
            
            num //= 2
            
        answer.append(string)
    return answer