def solution(n):
    answer = int(''.join(sorted(str(n))[::-1]))
    return answer