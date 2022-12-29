N, M = map(int, input().split())
numList = sorted(list(map(int, input().split())))

visited = [0]
used = [0] * N

def dfs(lev):
  if lev == M:
    print(*[ numList[i] for i in visited[1:]])
    return
  for i in range(visited[-1], N):
    visited.append(i)
    dfs(lev + 1)
    visited.pop()


dfs(0)