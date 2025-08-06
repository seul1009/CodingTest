n = int(input())
nums = list(map(int, input().split()))
x = int(input())

nums.sort()
s = 0
e = n - 1
count = 0

while s < e:
    total = nums[s] + nums[e]
    if total == x:
        count += 1
        s += 1
        e -= 1

    elif total < x:
        s += 1
    else:
        e -= 1
        
print(count)