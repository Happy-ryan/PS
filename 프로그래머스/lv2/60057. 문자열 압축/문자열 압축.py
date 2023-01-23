# aaabb 작은 케이스부터 해보자.
# ans에 넣은 가장 최근 값[-1]과 계속 비교하기.
def press(k, s):
    ans = []
    res = ''
    for i in range(0, len(s), k):
        x = s[i : i + k]
        if len(ans) == 0:
            ans.append(x)
        else:
            if ans[-1] == x:
                ans.append(x)
            else:
                ans.append('/') 
                ans.append(x)
    return ''.join(ans).split('/')

def solution(s):
    ans = len(s)
    for k in range(1, len(s)):
        cnt = 0
        for row in press(k, s):
            if len(row) > k:
                cnt += len(str(len(row)//k)) + k
            else:
                cnt += len(row)
        ans = min(ans, cnt)
    return ans