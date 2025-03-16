def solution(queries):
    def find(n, p):
        if n == 1:
            return "Rr"

        parent = find(n-1, (p-1)//4+1)
        idx = (p-1) % 4

        if parent == "RR":
            return "RR"
        elif parent == "rr":
            return "rr"
        else:
            return ["RR", "Rr", "Rr", "rr"][idx]

    return [find(n, p) for n, p in queries]