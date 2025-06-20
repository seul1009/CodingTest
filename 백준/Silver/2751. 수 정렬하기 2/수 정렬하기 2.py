import sys

input = sys.stdin.readline

num = []
n = int(input())
for i in range(n):
    num.append(int(input()))

num.sort()
for i in num:
    print(i)