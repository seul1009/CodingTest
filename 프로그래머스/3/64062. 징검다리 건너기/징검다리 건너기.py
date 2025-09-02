def solution(stones, k):
    s = 1
    e = max(stones)
    mid = (s + e) // 2
    
    while s <= e:
        cnt =0
        mid = (s +e) //2
        for stone in stones:
            if (stone - mid) <= 0:
                cnt += 1
                if cnt >= k:
                    e = mid -1
                    break
            else:
                cnt = 0
        else:
            s = mid + 1
    return s