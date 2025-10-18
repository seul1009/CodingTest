def solution(s):
    arr = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i,n in enumerate(arr):
        s = s.replace(n, str(i))
    return int(s)