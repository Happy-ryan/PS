def solution(n):
    answer = ''
    for x in range(1, n+1):
        if x % 2 != 0:
            answer += '수'
        else:
            answer += '박'
    return answer