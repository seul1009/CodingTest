import sys
input = sys.stdin.readline

# 트리 초기화
def initializeSegmentTree(index, start, end):
    if start == end:
        tree[index] = (nums[start], nums[start])
        return

    mid = (start + end)//2

    # 왼쪽 자식 노드 초기화
    initializeSegmentTree(index*2, start, mid)

    # 오른쪽 자식 노드 초기화
    initializeSegmentTree(index*2+1, mid+1, end)

    # 자식 노드의 결과를 이용해 현재 노드 구성
    tree[index] = (min(tree[index*2][0], tree[index*2+1][0]),
                   max(tree[index*2][1], tree[index*2+1][1]))

def queryInSegmentTree(index, range, start, end):

    # 완전히 포함되는 경우
    if range[0] <= start and end <= range[1]:
        return tree[index]

    mins, maxs = [], []
    mid = (start + end) // 2

    if range[0] <= mid and start <= range[1]:
        tmpMin, tmpMax = queryInSegmentTree(index*2, range, start, mid)
        mins.append(tmpMin)
        maxs.append(tmpMax)

    if range[0] <= end and mid+1 <= range[1]:
        tmpMin, tmpMax = queryInSegmentTree(index*2+1, range, mid+1, end)
        mins.append(tmpMin)
        maxs.append(tmpMax)

    return (min(mins), max(maxs))


n, m = map(int, input().split())
nums = [0] + [int(input()) for _ in range(n)]

tree = [(-1, -1)] * (4 * n)
initializeSegmentTree(1, 1, n)

for _ in range(m):
    a, b = map(int, input().split())
    print(*queryInSegmentTree(1, (a, b), 1, n))