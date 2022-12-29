# https://www.acmicpc.net/problem/15652
N, M = map(int, input().split())

visited = [1]


def dfs(lev):
    if lev == M:
        print(*visited[1:])
        return
  
    for i in range(visited[-1], N + 1):
        visited.append(i)
        dfs(lev + 1)
        visited.pop()

dfs(0)