import sys
sys.setrecursionlimit(10**4)

while True:
    a,b = map(int,input().split()) # a-열, b-행
    result =0
    if a==0 and b == 0:
        break
    adj = [input().split() for row in range(b)] # 다른 문제와 달리 입력이 공백을 가지고 들어오기 때문에 벽치기가 힘들다. 
                                                # 인덱스 0행0열부터~b-1행a-1열로 주의!
    visited=[[False for col in range(a)] for row in range(b)]

    dr = [-1,1,0,0,-1,1,-1,1] # 상/하/대각선
    dc = [0,0,-1,1,-1,1,1,-1] # 좌/우/대각선

    def adj_check(r,c):
        return 0<= r <= b-1 and  0<= c <= a-1
    
    def dfs(r,c):
        visited[r][c] = True
        for k in range(8):
            nr = r + dr[k]
            nc = c + dc[k]
            if adj_check(nr,nc) and\
                adj[nr][nc] == '1' and\
                    not visited[nr][nc]:
                    dfs(nr,nc)

    for r in range(0,b):
        for c in range(0,a):
            if adj[r][c] =='0' or visited[r][c]:
                continue
            dfs(r,c)
            result +=1
    print(result)