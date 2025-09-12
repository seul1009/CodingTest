from heapq import heappop, heappush
def solution(book_time):
    answer = 1
    
    for i in range(len(book_time)):
        book_time[i][0] = int(book_time[i][0].split(':')[0])*60 + int(book_time[i][0].split(':')[1])
        book_time[i][1] = int(book_time[i][1].split(':')[0])*60 + int(book_time[i][1].split(':')[1]) +10
    book_time.sort()
    print(book_time)
    
    heap = []
    for s, e in book_time:
        if not heap:
            heappush(heap,e)
            continue
        if heap[0] <= s:
            heappop(heap)
        else:
            answer += 1
        heappush(heap,e)
    return answer
        
        
        