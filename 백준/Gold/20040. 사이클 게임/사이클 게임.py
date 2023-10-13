import sys
sys.setrecursionlimit(10**4)

input = sys.stdin.readline

n,m = map(int,input().split())

par = [ i for i in range(n) ]
# time = []

def find(x):
    if x == par[x] : return x
    par[x] = find(par[x])
    return par[x]

def merge(a,b):
    # global time
    a,b = find(a), find(b)
    if a < b:
        par[b] = a # 작은 것이 루트노드
    else:
        par[a] = b
    # else: # 루트노드가 동일하면 사이클이 발생함.
    #     time.append(i)
    #     print(i)

for i in range(1,m+1):
    # if len(time) == 1:
    #     break
    a,b = map(int,input().split())
    if find(a) != find(b):
        merge(a,b)
    else:
        print(i)
        break
else:
    print(0)