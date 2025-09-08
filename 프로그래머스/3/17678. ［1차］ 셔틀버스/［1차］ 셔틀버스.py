from collections import deque

def to_minutes(time):
    h, m = map(int, time.split(":"))
    return h * 60 + m
    
def to_timestr(minutes):
    h = minutes // 60
    m = minutes % 60
    return f"{h:02d}:{m:02d}"
    
def solution(n, t, m, timetable):
    timetable = sorted([to_minutes(minute) for minute in timetable])
    shuttles = [540 + i * t for i in range(n)]
    queue = deque(timetable)
    
    for bus in shuttles:
        cnt = 0
        while queue and queue[0] <= bus and cnt < m:
            last = queue.popleft()
            cnt += 1
        
    
    if cnt < m:
        return to_timestr(shuttles[-1])
    else:
        return to_timestr(last - 1)
            
                
            
        
    
      