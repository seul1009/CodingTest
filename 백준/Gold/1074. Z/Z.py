def z(N, r, c):
    if N == 0:
        return 0   

    half = 2 ** (N - 1)
    block_size = half * half   

    # 1번 사분면
    if r < half and c < half:
        return z(N - 1, r, c)

    # 2번 사분면
    elif r < half and c >= half:
        return block_size + z(N - 1, r, c - half)

    # 3번 사분면
    elif r >= half and c < half:
        return 2 * block_size + z(N - 1, r - half, c)

    # 4번 사분면
    else:
        return 3 * block_size + z(N - 1, r - half, c - half)


N, r, c = map(int, input().split())
print(z(N, r, c))
