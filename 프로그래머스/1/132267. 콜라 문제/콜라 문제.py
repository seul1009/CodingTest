def solution(a, b, n):
    num=0
    while a<=n:
        num+=(n//a)*b
        n=(n//a)*b+(n%a)  
    return num    
         