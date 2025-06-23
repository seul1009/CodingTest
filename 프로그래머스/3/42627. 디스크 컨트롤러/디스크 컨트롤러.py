import heapq
def solution(jobs):
    heap = []
    now = 0
    idx = 0
    total = 0
    last = -1
    
    while idx < len(jobs):
        for job in jobs:
            if last < job[0] <= now:
                heapq.heappush(heap, [job[1], job[0]])
       
        if heap:
            current = heapq.heappop(heap)
            last = now
            now += current[0]
            total += now - current[1]
            idx += 1
        else:
            now += 1

    return total // len(jobs)