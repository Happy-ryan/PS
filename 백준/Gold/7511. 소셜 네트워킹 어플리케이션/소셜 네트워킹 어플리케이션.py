from collections import defaultdict

t = int(input())

def solution(n, friends, m, qs):
    
    par = [-1] * (n)
    
    # root 찾기
    def find(x):
        if par[x] == -1:
            return x
        par[x] = find(par[x])
        return par[x]
    
    def merge(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return False
        par[y] = x
        return True
    
    for a, b in friends:
        merge(a, b)
        
    dic = defaultdict(list)
    for idx, node in enumerate(par):
        # 해당 노드의 부모를 찾고 그 부모를 가진 그룹 만들기
        root = find(idx)
        dic[root].append(idx)
    
    # 같은 그룹 파악하는데 용이
    for a, b in qs:
        a = find(a)
        b = find(b)
        if a == b:
            print(1)
        else:
            print(0)
    
for i in range(t):
    n = int(input())
    k = int(input())
    friends = [list(map(int, input().split())) for _ in range(k)]
    m = int(input())
    qs = [list(map(int, input().split())) for _ in range(m)]
    print(f"Scenario {i + 1}:")
    solution(n, friends, m, qs)
    print()