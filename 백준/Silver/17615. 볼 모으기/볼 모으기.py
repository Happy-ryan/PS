n = int(input())
balls = list(input())

# RBBBBBBBBRRRRRRRRB

def solution(n, balls):
    # 그리디 - 빨간색끼리 / 파란색끼리..
    
    # case1 - 왼(R) / 오(B) * R 이동
    # case2 - 왼(R) / 오(B) * B 이동
    # case3 - 왼(B)) / 오(R) * R 이동
    # case4 - 왼(B) / 오(R) * B 이동
    # 총 4가지 case로 구성.
    
    def case1(mode):
        cnt = 0
        for ball in balls:
            if ball == mode:
                cnt += 1
            else:
                break
        return balls.count(mode) - cnt

    def case2(mode):
        cnt = 0
        for ball in balls[::-1]:
            if ball == mode:
                cnt += 1
            else:
                break
        return balls.count(mode) - cnt
    
    
    c1 = case1('R')
    c2 = case1('B')
    c3 = case2('R')
    c4 = case2('B')
    
    return min(c1, c2, c3, c4)

print(solution(n, balls))