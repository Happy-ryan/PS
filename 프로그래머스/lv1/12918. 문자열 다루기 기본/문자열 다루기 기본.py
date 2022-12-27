def solution(s):
    if len(s) == 4 or len(s) == 6:
        if s.isdigit(): # 문자열이 숫자로만 이루어졌는지 판단
            answer = True
        else:
            answer = False
    else:
        answer = False
    return answer