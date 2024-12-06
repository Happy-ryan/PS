from collections import Counter

def solution(s):
    dic = Counter(s)
    if ' ' in dic:
        dic.pop(' ')
    max_num = max(dic.values())
    flag = 0
    ans = ''
    for key, value in dic.items():
        if value == max_num:
            if flag == 0:
                ans = key
                flag = 1
            else:
                ans = '?'
    return ans

t = int(input())
for _ in range(t):
    s = input()
    print(solution(s))