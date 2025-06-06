from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
for _ in range(n):
    num, idx = map(int, input().split())
    priorities = list(map(int, input().split()))

    queue = deque((i, p) for i, p in enumerate(priorities))
    priorities.sort(reverse = True)

    i = 0

    while True:
        if queue[0][1] == priorities[i]:
            tmp = queue.popleft()[0]

            if tmp == idx:
                print(i + 1)
                break
            i += 1

        else:
            queue.rotate(-1)



