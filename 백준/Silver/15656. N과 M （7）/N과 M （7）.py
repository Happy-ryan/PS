N, M = map(int, input().split())
numList = sorted(list(map(int, input().split())))
used = [0] * N
visited = []


def dfs(lev):
    if lev == M:
        print(*[numList[i] for i in visited])
        return

    for i in range(0, N):
            visited.append(i)
            dfs(lev + 1)
            visited.pop()

dfs(0)