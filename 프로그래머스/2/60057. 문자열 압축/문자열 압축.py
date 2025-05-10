def solution(s):
    length = len(s)
    min_result = length  

    # 1부터 전체 길이의 절반까지
    for unit in range(1, length // 2 + 1):
        result = ""  
        prev = s[:unit] 
        count = 1

        for idx in range(unit, length, unit):
            current = s[idx:idx + unit]  

            if current == prev:
                count += 1
            else:
                if count > 1:
                    result += str(count) + prev
                else:
                    result += prev

                prev = current
                count = 1

        if count > 1:
            result += str(count) + prev
        else:
            result += prev

        min_result = min(min_result, len(result))

    return min_result
