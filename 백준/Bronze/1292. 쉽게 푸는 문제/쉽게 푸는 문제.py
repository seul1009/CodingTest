a, b = map(int, input().split())

num = [[i] * i for i in range(1, b + 1)]
snum = sum(num,[])
print(sum(snum[a-1 : b]))

