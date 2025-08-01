import sys
input = sys.stdin.readline

n = int(input())
HC = []

for _ in range(n):
    HC.append(list(map(int, input().split())))

for i in range(1, n):
    HC[i][0] = HC[i][0] + min(HC[i - 1][1], HC[i - 1][2])
    HC[i][1] = HC[i][1] + min(HC[i - 1][0], HC[i - 1][2])
    HC[i][2] = HC[i][2] + min(HC[i - 1][0], HC[i - 1][1])

print(min(HC[n-1]))