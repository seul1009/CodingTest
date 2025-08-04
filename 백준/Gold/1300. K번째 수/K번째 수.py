def kth_number(n, k):
    left, right = 1, n * n

    while left < right:
        mid = (left + right) // 2

        count = 0
        for i in range(1, n + 1):
            count += min(mid // i, n)

        if count < k:
            left = mid + 1
        else:
            right = mid

    return left

n = int(input())
k = int(input())
print(kth_number(n, k))
