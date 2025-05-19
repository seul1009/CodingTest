import sys

n = int(sys.stdin.readline())
s = []

for i in range(n):
    s.append(sys.stdin.readline().strip())
set_s = set(s)
s = list(set_s)
s.sort()
s.sort(key = len)
for i in s:
    print(i)