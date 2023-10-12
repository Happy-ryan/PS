# https://www.acmicpc.net/problem/9470
from copy import deepcopy
t = int(input())

def topological_sorting(K, M, P):
    adj = [[] for _ in range(M+1)]
    ind = [0 for _ in range(M+1)]
    strahler = [[] for _ in range(M+1)]
    for _ in range(P):
        A, B = map(int, input().split())
        adj[A].append(B)
        ind[B] += 1

    candidates = []
    for num in range(1, M+1):
        if ind[num] == 0:
            candidates.append(num)
            strahler[num].append(1)
    
    def calculate_level(num):
        k = max(strahler[num])
        if strahler[num].count(k) >= 2:
            return k + 1
        else:
            return k

    while candidates:
        cur = candidates.pop()
        level = calculate_level(cur)

        for nxt in adj[cur]:
            strahler[nxt].append(level)
            ind[nxt] -= 1
            if ind[nxt] == 0:
                candidates.append(nxt)
    return [K, calculate_level(M)]

for _ in range(t):
    K, M, P = map(int, input().split())
    print(*topological_sorting(K, M, P))