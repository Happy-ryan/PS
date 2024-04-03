# 이분탐색
# 현재 '나'의 색과 '나'의 인접 노드들과 색이 다른 그래프 > 이분그래프
# 따라서 사이클 탐색과 비슷하게
# 0 방문하지 않음 / 1 나의 색 / 2 인접 노드의 색
import sys
from collections import deque

sys.setrecursionlimit(10**5)

def solution(v, e, adj):
    
    visited = [0 for _ in range(v + 1)]
    
    def dfs(cur):
        
        for nxt in adj[cur]:
            if visited[nxt] == 0:
                visited[nxt] = visited[cur] % 2 + 1
                dfs(nxt)
                
    
    for cur in range(1, v + 1):
        # 색 칠해져있으면 가지마!
        if visited[cur] != 0:
            continue
        visited[cur] = 1
        dfs(cur)
    
    
    # print(visited)
        
    for cur in range(1, v + 1):
        for nxt in adj[cur]:
            if visited[nxt] == visited[cur]:
                return 'NO'
    
    return 'YES'

k = int(input())

for _ in range(k):
    v, e = map(int, input().split())
    adj = [[] for _ in range(v + 1)]
    for _ in range(e):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)
    print(solution(v, e, adj))