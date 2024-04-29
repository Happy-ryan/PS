import sys
sys.setrecursionlimit(10**5)

m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

def solution(n, m, board):
    
    dr = [1, 0]
    dc = [0, 1]
    
    visited = [[False for _ in range(m)] for _ in range(n)]
    
    def in_range(r, c):
        return 0 <= r < n and 0 <= c < m
    
    def dfs(r, c):
        visited[r][c] = True
        
        for k in range(2):
            nr = r + dr[k]
            nc = c + dc[k]
            if in_range(nr, nc) and not visited[nr][nc] and board[nr][nc] == 1:
                dfs(nr, nc)
            
    dfs(0, 0)
    
    if visited[n - 1][m - 1]:
        return 'Yes'
    return 'No'

print(solution(n, m, board))