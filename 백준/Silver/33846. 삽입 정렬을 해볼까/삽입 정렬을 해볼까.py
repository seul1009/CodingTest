import sys
input = sys.stdin.readline

n, t = map(int, input().split())
arr = list(map(int, input().split()))

answer = sorted(arr[:t]) + arr[t:]
print(*answer)
