n, m = map(int, input().split())
cmds = [list(map(int, input().split())) for _ in range(m)]

def solution(n, m, cmds):
    
    par = [-1] * (n + 1)
    sizes = [-1] * (n + 1)
    
    # root 찾기
    def find(x):
        # par[x]가 -1 이라는 것을 par[x] 가 root
        if par[x] == -1:
            return x
        # par[x]가 root가 아니면 par[x]의 root를 찾아야함
        root = find(par[x])
        par[x] = root # par[x]의 부모를 찾은 후에 넣어줌
        
        return root
    
    # 합
    def union(x, y):
        x = find(x) # x의 root
        y = find(y) # y의 root
        if x == y: # 이미 같은 부모 -> union 불필요
            return False
        # 부모가 다르면 한쪽에 붙여야함
        # y를 x 그룹에 넣으려고함 -> x그룹의 사이즈는 y그룹의 사이즈만큼 증가
        par[y] = x
        sizes[x] += sizes[y]
        return True # 잘 결합
    
    for cmd, a, b in cmds:
        if cmd == 0:
            union(a, b)
        else:
            if find(a) == find(b):
                print('YES')
            else:
                print('NO')
    
                
solution(n, m, cmds)