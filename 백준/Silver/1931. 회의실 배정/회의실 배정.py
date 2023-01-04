
N = int(input())
res = []
for _ in range(N):
    s, f = map(int,input().split())
    res.append((s, f))


def greedy(N, res):
    res.sort( key = lambda x : x[0])
    res.sort( key = lambda x : x[1])
    
    L = [0]
    for i in range(1, N):
        if res[L[-1]][1] <= res[i][0]:
            L.append(i) 
    return len(L)

print(greedy(N, res))