def solution(n, nums):
    adj = [[] for _ in range(n + 1)]
    for idx, num in enumerate(nums):
        adj[idx + 1].append(num)

    visited = [False for _ in range(n + 1)]

    def dfs(start):
        visited[start] = True

        for nxt in adj[start]:
            if not visited[nxt]:
                dfs(nxt)
    ans = 0
    for s in range(1, n + 1):
        if not visited[s]:
            dfs(s)
            ans += 1
    
    return ans


t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    print(solution(n, nums))