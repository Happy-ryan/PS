def solution(M, A, B):
    
    inf = 0.000000001
    
    t1 = (M / A) * 3600
    t2 = (M / B) * 3600
    
    t = abs(t1 - t2)
    
    def time(t):
        # t는 초를 의미함.
        h, m, s = 0, 0, 0
        
        h = t // 3600
        t %= 3600
        m = t // 60
        t %= 60
        s = round(t + inf)
        
        return f"{int(h)}:{int(m):02}:{int(s):02}"
    
    return time(t)

while True:
    M, A, B = map(int, input().split())
    if M == A == B == 0:
        break
    print(solution(M, A, B))