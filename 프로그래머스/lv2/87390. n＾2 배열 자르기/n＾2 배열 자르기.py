# n^7이므로 절대로 n^2 채울 수 없다. 규칙 발견 필요
# 인덱스 : (인덱스 // n = 행, 인덱스 % n = 열) mod연산! 아마도?
# (행, 열) 과 채워진 수의 관계성은?
# 채워진 수 = max( 행, 열 ) + 1
def cal(n, cur):
    r = cur // n
    c = cur % n
    return max(r, c) + 1

def solution(n, left, right):
    answer = []
    for i in range(left, right + 1):
        answer.append(cal(n, i))
    return answer