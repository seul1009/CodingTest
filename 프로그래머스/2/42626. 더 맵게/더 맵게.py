import heapq
def solution(scoville, K):
    h=[]
    for i in scoville:
        heapq.heappush(h, i)
    
    cnt=0
    while h[0]<K:
        heapq.heappush(h, heapq.heappop(h)+heapq.heappop(h)*2)
        cnt+=1
        
        if len(h) == 1 and h[0] < K:
            return -1
    return cnt
        
    