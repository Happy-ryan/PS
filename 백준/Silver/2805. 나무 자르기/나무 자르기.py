n, m = map(int, input().split())
Hs = list(map(int, input().split()))

def solution(n, m, Hs):
    
    # H의 정렬이 영향을 주지 아니함.
    Hs.sort()
    
    #10 15 17 20
    def cal(h):
        val = 0
        for H in Hs:
            val += max((H - h), 0)
        return val
    
    # h            14 15 | 16
    #              10  7 | 5
    #               T  T | F
    # print(cal(15))
    
    # 정답 영역 : l <= 여기에 부호
    # 정답 영역 l 이므로 출력은 r
    l, r = 0, 2000000000 + 1
    while l <= r:
        mid = (l + r) // 2
        if m > cal(mid): # mid를 줄여서 더 가져야함.
            r = mid - 1
        else:
            l = mid + 1
            
    return r 
    
            
print(solution(n, m, Hs))