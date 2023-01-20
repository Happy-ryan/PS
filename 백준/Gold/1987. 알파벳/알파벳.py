import sys

R, C = map(int, input().split())
maps = [ list(input()) for row in range(R)]

step = []
visited = [0] * 200
ans = 0

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def check(r, c):
    return 0 <= r < R and 0 <= c < C and visited[ord(maps[r][c])] == 0

def dfs(r, c):
    global ans
    cur = maps[r][c]
    visited[ord(cur)] = 1
    step.append(cur)
    ans = max(ans, len(step))

    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if check(nr, nc):
            dfs(nr, nc)
    # dfs 더 이상 갈 수 없음 > 백트래킹
    visited[ord(maps[r][c])] = 0
    step.pop()

dfs(0, 0)
print(ans)

# HFDFFB
# AJHGDH
# DGAGEH

# ['H'] 시작
# ['H', 'A']
# ['H', 'A', 'D']
# ['H', 'A', 'D', 'G']
# ['H', 'A', 'D', 'G', 'J']
# ['H', 'A', 'D', 'G', 'J', 'F'] 더 이상 dfs 불가능
# ['H', 'A', 'J'] # 백백백백 A로 이동 > J 움직임 
# ['H', 'A', 'J', 'F']
# ['H', 'A', 'J', 'F', 'D']
# ['H', 'A', 'J', 'G']
# ['H', 'A', 'J', 'G', 'D'] 더 이상 DFS 불가능
# ['H', 'F'] 백 백 백 백 H로 이동
# ['H', 'F', 'J']
# ['H', 'F', 'J', 'G']
# ['H', 'F', 'J', 'G', 'D']
# ['H', 'F', 'J', 'G', 'D', 'A']
# ['H', 'F', 'J', 'G', 'A']
# ['H', 'F', 'J', 'A']
# ['H', 'F', 'J', 'A', 'D']
# ['H', 'F', 'J', 'A', 'D', 'G']
# ['H', 'F', 'D']