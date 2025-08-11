n = input()
num = []

for i in n:
    num.append(i)
num.sort(reverse=True)
print("".join(num))
