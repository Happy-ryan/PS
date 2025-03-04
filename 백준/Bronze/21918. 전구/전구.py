n, m = map(int, input().split())
lis = list(map(int, input().split()))
qs = [list(map(int, input().split())) for _ in range(m)]

def solution(n, m, lis, qs):
    
    lis = [0] + lis
    # 4000 * 4000
    for q in qs:
        a, b, c = q
        if a == 1:
            lis[b] = c
        elif a == 2:
            for i in range(b, c + 1):
                lis[i] ^= 1
        elif a == 3:
            for i in range(b, c + 1):
                lis[i] = 0
        elif a == 4:
            for i in range(b, c + 1):
                lis[i] = 1
            
    return lis[1:]

print(*solution(n, m, lis, qs))