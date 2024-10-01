# 순열사이클
t = int(input())

def solution(n, nums):
    global cnt
    # 방향성 존재 - 그래프 생성
    adj = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        adj[i].append(nums[i - 1])
    
    def dfs(num):
        global cnt
        # 방문쳌
        visited[num] = True
        cnt += 1
        
        # 더 깊게..
        for x in adj[num]:
            if not visited[x]:
                dfs(x)

    visited = [False for _ in range(n + 1)]
    cnts = []
    for num in range(1, n + 1):
        cnt = 0
        # 방문안했으면 dfs 들어가자!
        if not visited[num]:
            dfs(num)
        cnts.append(cnt)

    ans = sum(1 for x in cnts if x != 0)
    
    return ans
    
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    print(solution(n, nums))