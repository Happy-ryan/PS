# "aya", "ye", "woo", "ma"
# 시작 : a / y / w / m  > 서로 겹치지 않는다.
def check(s):
    ans = []
    p = 0
    while p < len(s):
        if s[p] == 'a':
            ans.append(s[p : p + 3])
            p += 3
        elif s[p] == 'y':
            ans.append(s[p : p + 2])
            p += 2
        elif s[p] == 'w':
            ans.append(s[p : p + 3])
            p += 3
        elif s[p] == 'm':
            ans.append(s[p : p + 2])
            p += 2
        else:
            ans.append(s[p])
            p += 1
    return ans
# 연속 발음 판단 함수
def f(arr):
    flag = True # 연속된 것 없음
    for i in range(len(arr) - 1):
        if arr[i] == arr[i + 1]:
            flag = False
    return flag

def solution(babbling):
    answer = 0
    res = []
    for babble in babbling:
        flag = True
        if not f(check(babble)):
            flag = False
        else:
            for x in set(check(babble)):
                if x not in {"aya", "ye", "woo", "ma"}:
                    flag = False
        if flag:
            res.append(x)
            answer += 1
            
    return answer