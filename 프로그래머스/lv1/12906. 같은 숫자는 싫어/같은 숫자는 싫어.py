def solution(arr):
    answer = []
    for s in arr:
        if len(answer) == 0:
            answer.append(s)
        else:
            if answer[-1] == s:
                continue
            else:
                answer.append(s)
    return answer