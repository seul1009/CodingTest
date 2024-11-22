import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []
for i in range(n):
    x = int(input())
    if x == 0:
        if len(heap):
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, x)
