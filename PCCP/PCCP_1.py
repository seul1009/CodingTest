def solution(input_string):
    alp = set()
    lonely = set()

    prev = ''
    for string in input_string:
        if string != prev and string in alp:
            lonely.add(string)
        alp.add(string)
        prev = string

    return "".join(sorted(lonely)) if lonely else "N"

solution("eeddee")
