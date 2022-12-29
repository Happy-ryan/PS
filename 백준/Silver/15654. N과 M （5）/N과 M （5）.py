# https://www.acmicpc.net/problem/15652
N, M = map(int, input().split())
numList = sorted(list(map(int, input().split())))
used = [0] * N
visited = []


def dfs(lev):
    if lev == M:
        print(*[numList[i] for i in visited])
        return

    for i in range(0, N):
        if used[i] == 0:
            visited.append(i)
            used[i] = 1
            dfs(lev + 1)
            visited.pop()
            used[i] = 0

dfs(0)