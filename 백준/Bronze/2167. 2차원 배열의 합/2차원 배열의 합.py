N,M = map(int,input().split())
graph = [list(map(int,input().split())) for row in range(N)]

def psum(graph,i,j,x,y):
    sum = 0
    for r in range(i-1,x):
        for c in range(j-1,y):
            sum += graph[r][c]
    return sum

K = int(input())
for _ in range(K):
    i,j,x,y = map(int,input().split())
    print(psum(graph,i,j,x,y))
    