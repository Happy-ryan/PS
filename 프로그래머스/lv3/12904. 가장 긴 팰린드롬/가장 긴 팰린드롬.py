# 홀수 문자열(s)에서 팰린드롬 찾기
def isPalindrom(s, start):
    A = []
    l = start - 1
    r = start + 1
    flag = True
    while 0 <= l and r < len(s) and flag:
        if s[l] == s[r]:
            A.append(s[l: r + 1])
            l -= 1
            r += 1
        else:
            flag = False # 팰린드롬이 아니면 while 더 이상 돌 필요 없다.
    return A

def solution(s):
    answer = 1 # 문자열이 하나인 경우에는 isPalindrom에서 A = [] > solution함수에서 continue된다. 그러므로 기초값을 1로 잡자
    s = '#' + '#'.join(s) + '#' # 비교 편이성을 위해서
    print(s)
    for start in range(len(s)):
        if len(isPalindrom(s, start)) == 0: 
            continue
        # start에 따른 가장 긴 팰린드롬 뽑기
        x = isPalindrom(s, start)[-1]
        answer = max(answer, len(x) - x.count('#'))
    
    return answer

