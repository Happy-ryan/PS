import sys
input = sys.stdin.readline

N, M = map(int, input().split())

visited = []

def dfs(lev):
    if lev == M:
        print(*visited)
        return
    for i in range(1, N + 1):
        visited.append(i)
        dfs(lev + 1)
        visited.pop()

dfs(0)