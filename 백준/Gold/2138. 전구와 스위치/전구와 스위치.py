def change(b):
    return 0 if b == 1 else 1

def switch(bulb, x):
    for i in [x - 1, x, x + 1]:
        if 0 <= i < len(bulb):
            bulb[i] = change(bulb[i])

def simulate(now, goal, first):
    bulb = now[:]
    count = 0

    if first:
        switch(bulb, 0)
        count += 1

    for i in range(1, N):
        if bulb[i - 1] != goal[i - 1]:
            switch(bulb, i)
            count += 1

    return count if bulb == goal else float('inf')

N = int(input())
now = list(map(int, input()))
goal = list(map(int, input()))

res1 = simulate(now, goal, False)  # 0번 스위치 안 누름
res2 = simulate(now, goal, True)   # 0번 스위치 누름

answer = min(res1, res2)
print(answer if answer != float('inf') else -1)

