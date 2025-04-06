s = input()

def solution(s):
    n = len(s)
    w = s.count('a') # window 안에 a만 존재 = a의 총 갯수 = window 크기
    # 문자열 원형
    s = s + s

    # 1. 초기세팅
    pb = s[0:0 + w].count('b')
    cnt = int(1e18)
    
    for i in range(n):
        # 2. 조건 확인
        cnt = min(cnt, pb)
        
        # 3. 기존 칸 삭제
        if s[i] == 'b':
            pb -= 1
        # 4. 다음 칸 준비
        if s[i + w] == 'b':
            pb += 1
        
    return cnt

print(solution(s))