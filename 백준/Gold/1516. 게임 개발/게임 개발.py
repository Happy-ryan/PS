# https://www.acmicpc.net/problem/1516
n = int(input())
ind = [0 for _ in range(n + 1)]
adj = [[] for _ in range(n + 1)]
times = [0 for _ in range(n + 1)]
dp = [0 for _ in range(n + 1)]

for idx in range(1, n + 1):
    arr = list(map(int, input().split()))
    times[idx] += arr[0]
    nums = arr[1:-1]
    for num in nums:
        adj[num].append(idx)
        ind[idx] += 1

candidates = []
for num in range(1, n + 1):
    if ind[num] == 0:
        candidates.append(num)
        dp[num] = times[num]

result = []
while candidates:
    cur = candidates.pop()

    for nxt in adj[cur]:
        ind[nxt] -= 1
        dp[nxt] = max(dp[nxt], dp[cur] + times[nxt])
        if ind[nxt] == 0:
            candidates.append(nxt)


for time in dp[1:]:
    print(time)