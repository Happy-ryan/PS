from collections import deque

n,m,v = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(m)]
graph =[[0 for col in range(n+1)] for row in range(n+1)]
# print(arr)
# print(graph)
for row in arr:
    graph[row[0]][row[1]] = 1
    graph[row[1]][row[0]] = 1
# print(graph)

visted = [False]*(n+1)

def dfs(v):
    visted[v] = True
    print(v,end=' ')
    for i in range(1,len(graph[v])):
        if not visted[i] and graph[v][i]==1: # 방문하지 않음 & 노드가 연결이 되어 있어야함(1)
            dfs(i) 
dfs(v)

print()
visted = [False]*(n+1)
def bfs(v):
    queue = deque([v])
    visted[v] = True
    while queue:
        out = queue.popleft()
        print(out,end=' ')
        for i in range(1,len(graph[out])):
            if not visted[i] and graph[out][i] == 1:
                queue.append(i)
                visted[i] = True
bfs(v) 