import sys
sys.setrecursionlimit(10**5)

def solution(n, nums):
    adj = [[] for _ in range(n + 1)]
    # 0 방문하지않고 dfs 미진행
    # 1 방문 하는 중
    # 2 더 볼 필요가 없음.
    visited = [0 for _ in range(n + 1)]
    paths = []
    path = []
    
    for idx, num in enumerate(nums):
        adj[idx + 1].append(num)

    # 사이클을 찾아야한다.
    # 4 > 7 > 6 > 4
    # dfs(4) > dfs(7) > dfs(6) > dfs(4)
    # 그래프모양이 쭉 파고들다가 4로 컴백해야함.
    def dfs(start):
        if visited[start] == 2:
            return 
        visited[start] = 1
        path.append(start)

        for nxt in adj[start]:
            if visited[nxt] == 0:
                dfs(nxt)
            if visited[nxt] == 1:
                # nxt : 사이클의 시작점이 된다
                # nxt 이후 애들이 사이클이다
                # print(f"nxt: {nxt}, path: {path}")
                paths.extend(path[path.index(nxt):])
        # start 지점 - 더 들릴 필요 없다.
        visited[start] = 2
        path.pop()
        
        
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i)

    return n - len(paths)

t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    print(solution(n, nums))