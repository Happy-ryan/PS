def solution(s):
    answer1 = ''
    answer2 = ''
    for x in s:
        if x.isupper():
            answer2 += x
        else:
            answer1 += x
    answer = sorted(answer1)[::-1] + sorted(answer2)[::-1]
    final = ''.join(answer)
    return final