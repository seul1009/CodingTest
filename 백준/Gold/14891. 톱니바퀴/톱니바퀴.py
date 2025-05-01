from collections import deque
gears = [deque(list(map(int, input()))) for _ in range(4)]
k = int(input())
orders = [list(map(int, input().split())) for _ in range(k)]

def turn(wnum, direction):
    if direction == 1:
        gears[wnum].rotate(1)
    else:
        gears[wnum].rotate(-1)

def turn_left(wnum, l):
    if wnum < 0:
        return False
    if gears[wnum][2] != l:
        return True
    return False

def turn_right(wnum, r):
    if wnum > 3:
        return False
    if gears[wnum][-2] != r:
        return True
    return False

def direction_turn(wnum, direction):
    if wnum < 0 or wnum > 3:
        return
    r, l = gears[wnum][2], gears[wnum][-2]
    turn(wnum, direction)
    visited[wnum] = True

    if turn_right(wnum + 1, r) and visited[wnum + 1] == False:
        direction_turn(wnum + 1, -direction)

    if turn_left(wnum - 1, l) and visited[wnum - 1] == False:
        direction_turn(wnum - 1, -direction)
    return

for num, dir in orders:
    visited = [False] * 4
    direction_turn(num - 1, dir)

answer = 0
if gears[0][0]==1:
    answer+=1
if gears[1][0]==1:
    answer+=2
if gears[2][0]==1:
    answer+=4
if gears[3][0]==1:
    answer+=8
print(answer)