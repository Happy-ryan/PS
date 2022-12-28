def solution(food):
    final = ''
    answer = ''
    for i, k in enumerate(food):
        if i == 0: continue
        eat = k // 2
        answer += eat * str(i)
    final = answer + '0' + answer[::-1]
    return final