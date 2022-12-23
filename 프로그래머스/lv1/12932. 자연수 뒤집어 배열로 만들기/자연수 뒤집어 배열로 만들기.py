def solution(n):
    answer = []
    for k in reversed(str(n)):
        answer.append(int(k))
    return answer