N = int(input())
num = list(range(1, N + 1))
used = [0] * N
visited = []

def dfs(lev):
    if lev == N:
        print(*visited)
        return
    for i in range(N):
        if used[i] == 0:
            used[i] = 1
            visited.append(num[i])
            dfs(lev + 1)
            used[i] = 0
            visited.pop()

dfs(0)