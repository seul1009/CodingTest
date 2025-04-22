from collections import deque

def check(n, w, L, trucks):
    time = 0
    bridge = deque([0] * w)
    bridge_w = 0
    i = 0

    while i < n or bridge_w > 0:
        time += 1
        left = bridge.popleft()
        bridge_w -= left

        if i < n and bridge_w + trucks[i] <= L:
            bridge.append(trucks[i])
            bridge_w += trucks[i]
            i += 1
        else:
            bridge.append(0)

    return time

n, w, L = map(int, input().split())
trucks = list(map(int, input().split()))

print(check(n ,w, L, trucks))

