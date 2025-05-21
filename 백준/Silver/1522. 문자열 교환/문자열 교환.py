s = input()
n = len(s)
countA = s.count('a')

# 원형 처리를 위해 이어붙임
s += s

swap = countA

for i in range(n):
    countB = 0
    for j in range(countA):
        if s[i + j] == "b":
            countB += 1
    swap = min(swap, countB)

print(swap)