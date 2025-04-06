s = input()

def solution(s):
    n = len(s)
    w = s.count('a') # window 안에 a만 존재 = a의 총 갯수 = window 크기
    # 문자열 원형
    s = s + s
    
    inf = int(1e18)
    cnt = inf
    for i in range(n):
        p_b = s[i:i + w].count('b') # b -> a로 교화

        cnt = min(cnt, p_b)
    return cnt

print(solution(s))