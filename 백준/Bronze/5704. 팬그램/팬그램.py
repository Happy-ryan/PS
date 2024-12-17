from collections import Counter

def solution(s):
    dic = Counter(s)
    if dic[' ']:
        dic.pop(' ') # 공백제거
    if len(dic) >= 26:
        return 'Y'
    return 'N'

while True:
    s = input()
    if s == '*':
        break
    print(solution(s))