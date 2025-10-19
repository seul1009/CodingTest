def solution(record):
    dic={}
    result=[]
    
    for rec in record:
        record_split = rec.split()
        
        if len(record_split)==3:
            dic[record_split[1]] = record_split[2]
    
    for rec in record:
        record_split = rec.split()
        if record_split[0] == 'Enter':
            result.append(f'{dic[record_split[1]]}님이 들어왔습니다.')
        elif record_split[0] == 'Leave':
            result.append(f'{dic[record_split[1]]}님이 나갔습니다.')
    return result
        
        