
from collections import deque 

def solution(n, computers):
    answer = 0
    # adj : computers에서 얻은 연결요소 연결한 그래프(무방향성)
    adj = [[] for row in range(n)] 
    for r in range(n):
        for c in range(n):
            if r == c:  
                continue
            else:
                if computers[r][c] == 1:
                    adj[r].append(c)
                    
    in_queue = [False for col in range(n)]
    def bfs(x):
        q = deque([x])
        in_queue[x] = True
        
        while q:
            cx = q.popleft()
            for nx in adj[cx]:
                if in_queue[nx] == False:
                    q.append(nx)
                    in_queue[nx] = True
    
    for x in range(n):
        if in_queue[x] == False:
            bfs(x)
            answer += 1
        
    return answer
