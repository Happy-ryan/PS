from itertools import combinations
N = int(input())
matrix = [list(map(int, input().split())) for row in range(N)]

ans = int(1e18)
for row in combinations(list(range(N)), N//2):
    a = set(row)
    b = set(list(range(N))) - a
    teamA, teamB = 0, 0

    for i in a:
        for j in a:
            teamA += matrix[i][j]
        
    for i in b:
        for j in b:
            teamB += matrix[i][j]

    ans = min(ans, abs(teamA - teamB))
print(ans)