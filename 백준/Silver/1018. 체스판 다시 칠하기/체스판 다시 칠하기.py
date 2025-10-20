import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [input().strip() for _ in range(n)]

min_repaint = 64

for x in range(n - 7):
    for y in range(m - 7):
        white = 0
        black = 0

        for i in range(8):
            for j in range(8):
                current = board[x + i][y + j]

                # 행 + 열 = 짝수면 시작색과 같아야 함
                if (i + j) % 2 == 0:
                    if current != 'W':
                        white += 1
                    if current != 'B':
                        black += 1
                else:
                    if current != 'B':
                        white += 1
                    if current != 'W':
                        black += 1

        min_repaint = min(min_repaint, white, black)

print(min_repaint)

