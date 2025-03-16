def prevc(cur_time, op_start, op_end):
    if cur_time - 10 <= 0:
        cur_time = 0
    else:
        cur_time -= 10
        if op_start <= cur_time <= op_end:
            cur_time = op_end
    return cur_time


def nextc(video_len, cur_time, op_start, op_end):
    if cur_time + 10 >= video_len:
        cur_time = video_len
    else:
        if op_start <= cur_time <= op_end:
            cur_time = op_end + 10
        else:
            cur_time += 10
            if op_start <= cur_time <= op_end:
                cur_time = op_end
    return cur_time


def solution(video_len, pos, op_start, op_end, commands):
    video_len = int(video_len[0:2]) * 60 + int(video_len[3:5])
    pos = int(pos[0:2]) * 60 + int(pos[3:5])
    op_start = int(op_start[0:2]) * 60 + int(op_start[3:5])
    op_end = int(op_end[0:2]) * 60 + int(op_end[3:5])

    if pos >= op_start and pos < op_end:
        pos = op_end

    for command in commands:
        if command == "next":
            pos = nextc(video_len, pos, op_start, op_end)
        else:
            pos = prevc(pos, op_start, op_end)

    minutes = pos // 60
    seconds = pos % 60

    return f"{minutes:02}:{seconds:02}"