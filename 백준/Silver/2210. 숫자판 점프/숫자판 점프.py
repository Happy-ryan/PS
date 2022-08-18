adj = [ list(input().split()) for row in range(5)]

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def adj_check(r,c):
    return 0<= r < 5 and 0<= c < 5

def dfs(r,c,level):
    global s
    if level == 6:
        ans.add(s)
        return
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if adj_check(nr,nc):
                s += adj[nr][nc]
                dfs(nr,nc,level+1)
                s = s[:-1]


ans =set()

for r in range(5):
    for c in range(5):
        s = adj[r][c]
        dfs(r,c,1)

# print(ans)
sum = 0
for row in ans:
    if len(row) == 6:
        sum +=1

print(sum)