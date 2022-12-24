import math
def solution(n):
    x = math.sqrt(n)
    # 정수 판단 int(x) == x
    if int(x) == x:
        answer = (x+1)**2
    else:
        answer = -1
    return answer