import sys
from collections import deque

input = sys.stdin.readline

def solution(a, b):
    q = deque([(a, 1)])

    while q:
        n, cnt = q.popleft()
        if n == b:
            return cnt

        if n * 2 <= b:
            q.append((n * 2, cnt + 1))

        if n * 10 + 1 <= b:
            q.append((n * 10 + 1, cnt + 1))

    return -1


a, b = map(int, input().split())
print(solution(a, b))