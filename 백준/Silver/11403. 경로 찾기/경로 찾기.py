N = int(input())
inf = int(10e9)
graph = [ list(map(int,input().split())) for row in range(N)]
for a in range(N):
    for b in range(N):
        # if a==b:
        #     continue
        if graph[a][b] == 0:
            graph[a][b]= inf

for k in range(N):
    for a in range(N):
        for b in range(N):
            graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])

for a in range(N):
    for b in range(N):
        if graph[a][b] == inf:
            graph[a][b] = 0
        else:
            graph[a][b] = 1

for row in graph:
    print(*row)