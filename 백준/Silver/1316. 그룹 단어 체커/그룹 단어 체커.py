import sys
input = sys.stdin.readline

def check_group_word(word):
    seen = set()
    prev = None
    for ch in word:
        if ch != prev:
            if ch in seen:
                return False
            if prev is not None:
                seen.add(prev)
            prev = ch
    return True

n = int(input().strip())
cnt = 0
for _ in range(n):
    w = input().strip()
    if check_group_word(w):
        cnt += 1
print(cnt)
