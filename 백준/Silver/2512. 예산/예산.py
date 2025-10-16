n = int(input())
regions = list(map(int, input().split()))
m = int(input())

start, end = 1, max(regions)
result = 0
while start <= end:
    budget = 0
    mid = (start + end) // 2

    for region in regions:
        budget += min(region, mid)

    if budget <= m:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)