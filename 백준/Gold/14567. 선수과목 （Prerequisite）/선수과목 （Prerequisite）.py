# https://www.acmicpc.net/problem/14567
n, m = map(int, input().split())

adj = [[] for _ in range(n + 1)]
ind = [0 for _ in range(n + 1)]
dp = [1 for _ in range(n + 1)]
dp[0] = 0 

# 선수과목(A) - 비선수과목(B)
for _ in range(m):
    A, B = map(int, input().split())
    adj[A].append(B)
    ind[B] += 1

# 후보군 넣기
candidates = []
for x in range(1, n + 1):
    if ind[x] == 0:
        candidates.append(x)

# 결과값 리스트 만들기
# candidates 비우기
results = []
while candidates:
    cur = candidates.pop()
    results.append(cur)
    
    for nxt in adj[cur]:
        ind[nxt] -= 1
        dp[nxt] = max(dp[nxt], dp[cur] + 1)
        if ind[nxt] == 0:
            candidates.append(nxt)
            
print(*dp[1:])