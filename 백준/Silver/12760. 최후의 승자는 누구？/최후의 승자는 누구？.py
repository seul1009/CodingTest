n, m = map(int, input().split())
players = []

for i in range(n):
    nums = list(map(int, input().split()))
    nums.sort(reverse=True)
    players.append(nums)

score = [0] * n

for i in range(m):
    cards = [players[p][i] for p in range(n)]
    max_card = max(cards)

    for p in range(n):
        if cards[p] == max_card:
            score[p] += 1

max_score = max(score)
winners = [str(i+1) for i, s in enumerate(score) if s == max_score]

print(" ".join(winners))




