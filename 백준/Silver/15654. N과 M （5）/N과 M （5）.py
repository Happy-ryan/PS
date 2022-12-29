# https://www.acmicpc.net/problem/15652
N, M = map(int, input().split())
numList = sorted(list(map(int, input().split())))
used = [0] * N
visited = []


def dfs(lev):
    if lev == M:
        print(*visited)
        
    for i, num in enumerate(numList):
        if used[i] == 0:
            visited.append(num)
            used[i] = 1
            dfs(lev + 1)
            visited.pop()
            used[i] = 0

dfs(0)