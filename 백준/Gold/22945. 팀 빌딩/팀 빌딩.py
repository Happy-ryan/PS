n = int(input())
Xs = list(map(int, input().split()))

def solution(n, Xs):
    # 정렬하면 안된다.
    capa = 0
    l = 0
    r = n - 1
    # for l in range(n):
    #     while l + 1 < r and Xs[l] > Xs[r]:
    #         r -= 1
    while l < r:
        capa = max(capa, (r - l - 1) * min(Xs[l], Xs[r]))
        
        if Xs[l] < Xs[r]:
            l += 1
        else:
            r -= 1
    
    return capa

print(solution(n, Xs))