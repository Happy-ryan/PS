from collections import deque

n, s, m = map(int, input().split())
vols = list(map(int, input().split())) + [0]


def solution_1(n, s, m, vols):

    visited = [[False for _ in range(m + 1)] for _ in range(n + 1)]

    def in_range(r, c):
        return 0 <= r < n + 1 and 0 <= c < m + 1

    def dfs(r, c):
        visited[r][c] = True

        vol_1 = c + vols[r]
        vol_2 = c - vols[r]
        if in_range(r + 1, vol_1) and not visited[r + 1][vol_1]:
            dfs(r + 1, vol_1)
        if in_range(r + 1, vol_2) and not visited[r + 1][vol_2]: 
            dfs(r + 1, vol_2)

    dfs(0, s)
    
    row = visited[n][::-1]
    
    try:
        return m - row.index(True)
    except:
        return -1


print(solution_1(n, s, m, vols))
