def solution(s):
    x = len(s)//2
    if len(s) % 2 == 0:
        answer = s[x-1:x+1]
    else:
        answer = s[x]
    return answer