import heapq
n = int(input())
q = []
count = 0
for num in map(int, input().split()):
    heapq.heappush(q, num)

for _ in range(n-1):
    nums = list(map(int, input().split()))
    for num in nums:
        if q[0] < num:
            heapq.heappop(q)
            heapq.heappush(q, num)
print(q[0])





