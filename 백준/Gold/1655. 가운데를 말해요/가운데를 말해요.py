import heapq
import sys

input = sys.stdin.readline

n = int(input())
max_heap = []
min_heap = []

for i in range(n):
    num = int(input())
    if i % 2 == 0:
        heapq.heappush(max_heap,-num)
    else:
        heapq.heappush(min_heap,num)

    if max_heap and min_heap and -max_heap[0] > min_heap[0]:
        rvalue = -heapq.heappop(max_heap)
        lvalue = heapq.heappop(min_heap)

        heapq.heappush(max_heap,-lvalue)
        heapq.heappush(min_heap,rvalue)

    print(-max_heap[0])

