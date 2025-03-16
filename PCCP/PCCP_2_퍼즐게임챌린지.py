def time_check(diffs, times, limit, level):
    time = 0
    for i in range(len(diffs)):
        if diffs[i] <= level:
            time += times[i]
        if diffs[i] > level:
            time += (times[i - 1] + times[i]) * (diffs[i] - level) + times[i]
        if time > limit:
            return False
    return True

def solution(diffs, times, limit):
    start, end = min(diffs), max(diffs)

    while start <= end:
        level = (start + end) // 2
        if time_check(diffs, times, limit, level):
            end = level - 1
        else:
            start = level + 1

    return start

