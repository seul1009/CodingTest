import sys
import math

input = sys.stdin.readline
n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    lcm = a * b // math.gcd(a, b)
    print(lcm)
