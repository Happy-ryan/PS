n = int(input())
# 0 base 주의
adj = list(map(int,input().split()))
in_queue = [False]*n  
dist = [0]*n

def adj_check(cur):
    return 0<= cur < n

from collections import deque
q = deque([0])
in_queue[0] = True
# cur 인덱스 의미
while q:
    cur = q.popleft()
    for nxt in range(cur+1,cur+adj[cur]+1): # 점프할 수 있는 range
        if adj_check(nxt) and\
            not in_queue[nxt]:
            q.append(nxt)
            in_queue[nxt] = True
            dist[nxt] = dist[cur] + 1

if not in_queue[-1]:
    print(-1)
else:
    print(dist[-1])