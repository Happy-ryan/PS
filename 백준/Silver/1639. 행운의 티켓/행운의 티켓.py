# https://www.acmicpc.net/problem/1639

s = input()

def str_cum(s):
    cnt = 0
    for x in s:
        cnt += int(x)
    return cnt

def f(k, s):
    flag = False
    for i in range(0, len(s) - k + 1):
        row = s[i : i + k]
        if str_cum(row[: len(row)//2]) == str_cum(row[len(row)//2:]):
            flag = True
    if flag:
        return k
    else:
        return 0

ans = 0
for k in range(2, len(s) + 1, 2):
    ans = max(ans, f(k, s))
    
print(ans)