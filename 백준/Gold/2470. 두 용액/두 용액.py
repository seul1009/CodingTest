n = int(input())
sol = list(map(int, input().split()))
sol.sort()

start = 0
end = n - 1
min_solution = float('inf')

while start < end:
    s = sol[start] + sol[end]
    if abs(s) < min_solution:
        min_solution = abs(s)
        result = [sol[start], sol[end]]
    if s < 0:
        start += 1
    elif s > 0:
        end -= 1
    else:
        break

print(result[0], result[1])