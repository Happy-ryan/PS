from collections import deque
T = int(input())
for _ in range(T):
    N,M = map(int,input().split())
    adj =[[] for row in range(N+1)]
    for _ in range(M):
        a,b = map(int,input().split())
        adj[a].append(b)
        adj[b].append(a)
    
    # result = []

    # for cur in range(1,N+1):
    #     in_queue = [False]*(N+1)
    #     q = deque([cur])
    #     in_queue[cur] = True
    #     cnt = 0
    #     while q:
    #         v = q.popleft()
    #         for nxt in adj[v]:
    #             if not in_queue[nxt]:
    #                 q.append(nxt)
    #                 in_queue[nxt] = True
    #         cnt += 1
    #     result.append(cnt)

    # print(cnt-1)
    print(N - 1)