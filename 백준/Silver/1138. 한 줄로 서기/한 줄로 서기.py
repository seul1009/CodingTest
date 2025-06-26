n = int(input())
arr = list(map(int, input().split()))

line = []

for i in range(n-1, -1, -1):
    line.insert(arr[i], i+1)

print(*line)
