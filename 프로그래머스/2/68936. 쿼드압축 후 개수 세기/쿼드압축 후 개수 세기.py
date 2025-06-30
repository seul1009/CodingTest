def solution(arr):
    n = len(arr)
    result = [0, 0]  

    def is_all_same(x, y, size):
        first = arr[x][y]
        for i in range(x, x + size):
            for j in range(y, y + size):
                if arr[i][j] != first:
                    return False
        return True

    def divide_and_count(x, y, size):
        if is_all_same(x, y, size):
            result[arr[x][y]] += 1
            return
        
        half = size // 2
        divide_and_count(x, y, half)
        divide_and_count(x, y + half, half)
        divide_and_count(x + half, y, half)
        divide_and_count(x + half, y + half, half)

    divide_and_count(0, 0, n)
    return result