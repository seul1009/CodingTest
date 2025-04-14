k, n = map(int, input().split())

LAN = [int(input()) for _ in range(k)]
def numberOfLAN(m):
    count = 0
    for i in LAN:
        count += i // m
    return count

s = 1; e = max(LAN)

while s <= e:
    m = (s + e) // 2
    c = numberOfLAN(m)
    if c >= n:
        maxLAN = m
        s = m + 1
    else:
        e = m - 1

print(maxLAN)