def solution(friends, gifts):
    gift_count = {f: [0, 0] for f in friends}
    record = {f: {g: 0 for g in friends} for f in friends}
    
    for gift in gifts:
        sender, receiver = gift.split()
        gift_count[sender][0] += 1
        gift_count[receiver][1] += 1
        record[sender][receiver] += 1
    
    gift_index = {f: gift_count[f][0] - gift_count[f][1] for f in friends}
    
    next_month = {f: 0 for f in friends}
        
    for i in range(len(friends)):
        for j in range(i+1, len(friends)):
            A, B = friends[i], friends[j]
            
            if record[A][B] > record[B][A]:
                next_month[A] += 1
            elif record[A][B] < record[B][A]:
                next_month[B] += 1
            else:
                if gift_index[A] > gift_index[B]:
                    next_month[A] += 1
                elif gift_index[A] < gift_index[B]:
                    next_month[B] += 1

    return max(next_month.values())

            
        
        