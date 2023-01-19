# 짝수 문자열 > 홀수 문자열
def padding(arr):
    ans = '#'
    for x in arr:
        ans += x
        ans += '#'
    return ans

# 홀수 문자열(s)에서 팰린드롬 찾기
def isPalindrom(s, start):
    A = []
    l = start - 1
    r = start + 1
    flag = True
    while 0 <= l and r < len(s) and flag:
        if s[l] == s[r]:
            A.append(s[l : r + 1])
            l -= 1
            r += 1
        else:
            flag = False
    return A

def solution(s):
    answer = 1 # 문자열이 하나인 경우에는 isPalindrom에서 A = [] > solution함수에서 continue된다. 그러므로 기초값을 1로 잡자
    if len(s) % 2 == 0: # s의 길이 짝수 > padding
        s = padding(s)
        
    for i in range(len(s)):
        if len(isPalindrom(s, i)) == 0: 
            continue
        # start에 따른 가장 긴 팰린드롬 뽑기
        x = isPalindrom(s, i)[-1]
        # 홀수문자열에서는 padding없으므로 #의 개수 0
        answer = max(answer, len(x) - x.count('#'))
    
    return answer