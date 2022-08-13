import sys
sys.setrecursionlimit(10**5)

R,C = map(int,input().split())
adj = [list(input()) for row in range(R)]
# print(adj)

visited = [[False for col in range(C)] for row in range(R)]

dr = [-1,1,0,0]
dc = [0,0,-1,1]


def adj_check(r,c):
    return 0<= r <= R-1 and 0<= c <= C-1


def dfs(r,c):
    global o_num, v_num
    visited[r][c] = True
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if adj_check(nr,nc) and\
            not visited[nr][nc] and\
                adj[nr][nc] != '#':
                if adj[nr][nc] == 'v':
                    v_num += 1
                elif adj[nr][nc] == 'o':
                    o_num += 1
                dfs(nr,nc)

final_v = 0
final_o = 0        
for r in range(0,R):
    for c in range(0,C):
        if visited[r][c] or adj[r][c] == '#':
            continue
        if adj[r][c] == 'v':
            v_num = 1 # 늑대
            o_num = 0 # 양
        elif adj[r][c] =='o':
            v_num = 0 # 늑대
            o_num = 1 # 양
        else: 
            v_num, o_num = 0,0
        # dfs는 잘 설계됐는데 처음에 v를 만나면 1개를 세고 가야하는데 if문을 두지 않으면 세지 않고 넘어가게 된다.
        # 따라서 v나o로 dfs를 시작하게 되면 변수를 1로 만들어주고 시작해야한다.
        dfs(r,c)
        # dfs 탈출하고 양의 수와 늑대의 수 비교해서 최종 숫자에 더하기
        if o_num > v_num:
            final_o += o_num
            final_v += 0
        else:
            final_o += 0
            final_v += v_num
    
print(final_o, final_v)

