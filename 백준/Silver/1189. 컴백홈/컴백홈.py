# https://www.acmicpc.net/problem/1189

# K와 k 변수명 주의...
R, C, K = map(int, input().split())
road = [list(input()) for row in range(R)]
visited = [[False for col in range(C)] for row in range(R)]

def check(r, c, road):
    return 0<= r < len(road) and 0<= c < len(road[0]) and road[r][c] == "."

def dfs(r, c, road,  level, K):
    # K - 1 깊이만큼 오면 무조건 종료는 되어야한다. 그러므로 앞조건과 뒷조건은 나눠서 체크해야함,
    if level == (K - 1):
        if r == 0 and c == len(road[0]) - 1:
            return 1
        else:
            return 0
    ret = 0
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    visited[r][c] = True
    for k in range(4):
        nr, nc = r + dr[k], c + dc[k]
        if check(nr, nc, road) and not visited[nr][nc]:
            ret += dfs(nr, nc, road, level + 1, K)
    visited[r][c] = False
    
    return ret

print(dfs(R-1, 0, road, 0, K))
