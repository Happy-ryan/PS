n, m = map(int, input().split())
jws = [int(input()) for _ in range(m)]

def solution(n, m, jws):
    
    def cal(x):
        # 한 사람 당 최대 x개(=질투)씩 가져갈 때 질투의 수를 계산
        num = 0
        for jw in jws:
            num += jw // x
            if jw % x != 0:
                num += 1

        return num
    
    inf = int(1e10) + 1
    
    l, r = 1, inf
    while l <= r:
        m = (l + r) // 2
        # 정답영역 : 
        if cal(m) <= n:
            r = m - 1
        else:
            l =  m + 1
        
    return l
    
print(solution(n, m, jws))