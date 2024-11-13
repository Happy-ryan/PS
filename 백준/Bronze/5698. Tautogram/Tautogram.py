def solution(s):
    flag = s[0][0].lower()
    for x in s[1:]:
        if flag != x.lower()[0]:
            return 'N'
    return 'Y'

while True:
    s = list(input().split())
    if s[0] == '*':
        break
    print(solution(s))