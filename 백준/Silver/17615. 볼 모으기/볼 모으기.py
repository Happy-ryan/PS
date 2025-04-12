n = int(input())
balls = list(input())

def solution(n, balls):
    # 그리디 - 빨간색끼리 / 파란색끼리..
    
    # 최대 이동 수 = 선택한 색의 공의 전체 수.
    
    # 'R'RRRR...RRB.....'B'
    # 한 쪽은 파란색 / 한 쪽은 빨간색
    
    # case1. R - B / B - R
    # min(R, B)
    
    # case2. R - R / B - B
    # R - R ... 반드시 R 선택! R[R의 수1] ~ [R의수 3] ~ [R의 수 2]R
    # min(R1, R2) + R3
    
    # B BRBBBB R
    
    def check(mode):
        # case1
        if balls[0] != balls[-1]:
            cnt = balls.count(mode)
            return min(cnt - 1, n -cnt - 1)
        
        if balls[0] == balls[-1]:
            cnt1 = 0
            for i in range(n):
                if balls[i] == mode:
                    cnt1 += 1
                else:
                    break
            cnt3 = 0
            for i in range(n - 1, -1, -1):
                if balls[i] == mode:
                    cnt3 += 1
                else:
                    break
                    
            cnt2 = balls.count(mode) - cnt1 - cnt3
            
            # print("왼", cnt1)
            # print("중", cnt2)
            # print("오", cnt3)
            return cnt2 + min(cnt1, cnt3)
        
    red = check('R')
    blue = check('B')
    
    # print(red)
    # print(blue)
    
    return min(red, blue)
    
print(solution(n, balls))