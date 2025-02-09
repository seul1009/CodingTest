n, m = map(int, input().split())
tree_list = list(map(int, input().split()))

left = 0
right = max(tree_list)
answer = 0

while left <= right:
    tree_sum = 0
    h = (left + right) // 2
    for tree in tree_list:
        if tree > h:
            tree_sum += tree - h

    if tree_sum < m :
        right = h - 1
    else:
        answer = h
        left = h + 1
print(answer)

