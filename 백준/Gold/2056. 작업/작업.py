# https://www.acmicpc.net/problem/2056
n = int(input())
jobs = [list(map(int, input().split())) for _ in range(n)]

adj = [[] for _ in range(n+1)]
ind = [0 for _ in range(n+1)]
times =[0 for _ in range(n+1)]
dp = [0 for _ in range(n+1)]

for idx, job in enumerate(jobs):
    t = job[0]
    times[idx+1] = t
    
    cnt = job[1]
    ind[idx+1] = cnt
    
    nums = job[2:]
    for num in nums:
        adj[num].append(idx+1)
        
candidates = []
for num in range(1, n+1):
    if ind[num] == 0:
        candidates.append(num)
        dp[num] = times[num]
        
while candidates:
    cur = candidates.pop()
    
    for nxt in adj[cur]:
        ind[nxt] -= 1
        dp[nxt] = max(dp[nxt], dp[cur]+times[nxt])
        if ind[nxt] == 0:
            candidates.append(nxt)

print(max(dp))