yname = input().rstrip()
n = int(input())
team_name = {}

for _ in range(n):
    tname = input()
    name = yname + tname

    L = name.count('L')
    O = name.count('O')
    V = name.count('V')
    E = name.count('E')

    team_name[tname] = ((L + O) * (L + V) * (L + E) * (O + V) * (O + E) * (V + E)) % 100

team = sorted(team_name.items(), key=lambda x: (-x[1], x[0]))
print(team[0][0])

