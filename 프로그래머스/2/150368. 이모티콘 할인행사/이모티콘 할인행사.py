def solution(users, emoticons):
    discount = [10, 20, 30, 40]
    max_plus = 0
    max_sales = 0
    n = len(emoticons)
    rates = [0] * n
    
    def dfs(idx):
        nonlocal max_plus, max_sales
        
        if idx == n:
            plus, sales = check(users, emoticons, rates)
            
            if plus > max_plus or (plus == max_plus and sales > max_sales):
                max_plus, max_sales = plus, sales
            return
        
        for d in discount:
            rates[idx] = d
            dfs(idx + 1)

    def check(users, emoticons, rates):
        plus_cnt = 0     
        total_sales = 0
        
        for percent, limit in users:
            total = 0

            for i in range(len(emoticons)):
                if rates[i] >= percent:
                    total += emoticons[i] * (100 - rates[i]) / 100

            if total >= limit:
                plus_cnt += 1
            else:
                total_sales += int(total)

        return plus_cnt, total_sales

    dfs(0)
    return [max_plus, max_sales]