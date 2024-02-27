# 물의 영역을 모조리 찾고 물의 영역에서 4방향에 존재하는 빙하의 높이를 줄인다!
# 1단계: 물의 영역을 찾는 그래프 탐색
# 2단계: 물의 영역이 빙하에 미치는 영향 갱신하기
from collections import deque
import sys
sys.setrecursionlimit(10**5)

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# 배열의 첫 번째행과 열, 마지막 행과 열은 0으로만 채워짐

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def in_range(r, c, n, m):
    return 0 <= r < n and 0 <= c < m


def find_ice(n, m):
    
    visited = [[False for _ in range(m)] for _ in range(n)]
    
    def dfs(r, c):
        visited[r][c] = True
        cnt[0] += 1 # 방문시 +1
        ices.append((r, c)) # 방문시 좌표처리
        
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if in_range(nr, nc, n, m) and not visited[nr][nc] and board[nr][nc] != 0:
                dfs(nr, nc)

    ices = []
    cnts = []
    for r in range(n):
        # 열은 m이다! 행과열 다를 때 주의하기!
        for c in range(m):
            if visited[r][c] or board[r][c] == 0:
                continue
            cnt = [0]
            dfs(r, c)
            cnts.append(cnt[0])

    return ices, len(cnts)



def solution(n, m, board):

    t = 0
    while True:
        
        ices, ice_group = find_ice(n, m)
                
        if ice_group >= 2:
            return t
        
        if ice_group == 0:
            return 0
        
        t += 1
        melt = []
        for r, c in ices:
            cnt = 0
            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]
                if in_range(nr, nc, n, m) and board[nr][nc] == 0:
                    # r, c가 현재 빙하 위치이며 nr, nc는 물을 찾는 곳임
                    # 빙하의 높이가 줄어들어야함으로 nr, nc를 줄이면 안된다.
                    cnt += 1
            melt.append((r, c, cnt))
        # 빙하를 동시에 녹여야한다.
        # 하나씩 녹이면 높이가 1인 경우, 먼저0으로 변경되어 다른 빙하에 영향을 주기때문이다.
        for i, j, cnt in melt:
            board[i][j] = max(0, board[i][j] - cnt)
                
        # for row in board:
        #     print(row)
        # print("=")

print(solution(n, m, board))