# https://www.acmicpc.net/problem/1005
t = int(input())
for _ in range(t):
    N, K = map(int, input().split())
    adj = [[] for _ in range(N + 1)]
    ind = [0 for _ in range(N + 1)]
    dp = [0 for _ in range(N + 1)]
    times = ['인덱스용'] + list(map(int, input().split()))
    for _ in range(K):
        X, Y = map(int, input().split())
        adj[X].append(Y)
        ind[Y] += 1
    W = int(input())
    # 후보군 넣기
    candidates = []
    for num in range(1, N + 1):
        if ind[num] == 0:
            candidates.append(num)
            dp[num] = times[num]
    # candidates 확인  
    result = []
    while candidates:
        cur = candidates.pop()
        result.append(cur)
        
        for nxt in adj[cur]:
            ind[nxt] -= 1
            # times[nxt] 반드시 더해져야함. 어디에? 내 현재 누적 시간에다가.
            # dp[nxt]가 갱신되어야함. 
            dp[nxt] = max(dp[nxt], times[nxt] + dp[cur])
            if ind[nxt] == 0:
                candidates.append(nxt)

    print(dp[W])