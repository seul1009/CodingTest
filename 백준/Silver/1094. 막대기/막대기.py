import heapq

X = int(input())

sticks = [64]

while X != sum(sticks):
    if sum(sticks) > X:
        min_sticks = heapq.heappop(sticks)
        half = min_sticks // 2
        if sum(sticks) + half >= X:
            heapq.heappush(sticks, half)

        else:
            heapq.heappush(sticks, half)
            heapq.heappush(sticks, half)

print(len(sticks))
