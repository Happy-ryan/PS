N,M = map(int,input().split())
adj =[[] for row in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    # a가 b를 신뢰한다 > b 해킹하면 a도 해킹 가능
    adj[b].append(a)
# print(adj)
result = [0]
from collections import deque
for x in range(1,N+1):
    in_queue = [False]*(N+1)
    q = deque([x])
    in_queue[x] = True
    cnt = 1
    while q:
        cur = q.popleft()
        for nxt in adj[cur]:
            if not in_queue[nxt]:
                q.append(nxt)
                in_queue[nxt] = True
                cnt += 1
    result.append(cnt)

# print(result)
max_result = max(result)
for k in range(1,N+1):
    if result[k] >= max_result:
        print(k, end=' ')