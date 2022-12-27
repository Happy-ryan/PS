def f(x):
    cnt = 0
    for k in range(1, x+1):
        if x % k == 0:
            cnt += 1
    return cnt

def solution(left, right):
    answer = 0
    for x in range(left, right + 1):
        if f(x) % 2 == 0:
            answer += x
        else:
            answer -= x
    return answer