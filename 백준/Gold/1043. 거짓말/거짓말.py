n, m = map(int, input().split())
infos = list(map(int, input().split())) # 진실을 아는자 + 번호...
edges = [list(map(int, input().split())) for _ in range(m)]

def solution(n, m, infos, edges):
    # 파티(그룹) + 거짓말 최대한 많이!! -> 그룹 + 최소(최대)) 한전
    # 진실을 아는 자와 파티를 덜 만나야함!
    
    if infos[0] == 0:
        return m
    
    # 기본공식
    par = [-1] * (n + 1)
    sizes = [-1] * (n + 1)
    
    def find(x):
        if par[x] == -1:
            return x
        
        root = find(par[x])
        par[x] = root
        
        return root
    
    def union(x, y):
        x = find(x)
        y = find(y)
        
        if x == y:
            return False
        
        if sizes[x] < sizes[y]:
            x, y = y, x
            
        par[y] = x
        sizes[y] += sizes[x]
        
        return True
    
    # 그냥 그룹
    for row in edges:
        _, people = row[0], row[1:]
        for i in range(len(people) - 1):
                union(people[i], people[i + 1])
                
    # 진실아는그룹
    for i in range(1, len(infos) - 1):
        union(infos[i], infos[i + 1])
    
    root = find(infos[1])

    cnt = 0
    for row in edges:
        _, person = row[0], find(row[1])
        if  root != person: 
            cnt += 1
            
    return cnt
    

print(solution(n, m, infos, edges))
        
        
        
        