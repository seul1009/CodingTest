n = int(input())
xlist = list(map(int, input().split()))
sorted_x = sorted(set(xlist))

dic = {}

for i in range(len(sorted_x)):
    dic[sorted_x[i]] = i

for i in xlist:
    print(dic[i], end=" ")

