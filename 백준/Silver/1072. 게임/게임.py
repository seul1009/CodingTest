import sys
input = sys.stdin.readline

# x: 게임 횟수, y: 이긴 게임
x, y = map(int, input().split())
z = y * 100 // x # 승률

if z >= 99:
    print(-1)
else:
    left, right = 1, x # 최소 1판부터 최대 x판까지 추가
    answer = -1

    while left <= right:

        mid = (left + right) // 2 
        new_z = (y + mid) * 100 //(x + mid)

        if new_z > z:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    print(answer)