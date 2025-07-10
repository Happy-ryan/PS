# 남규 >= 영훈 + 2
# 남는 사탕 없고 / 0개 받는 사람 없고
# 택희 = 짝수

N = int(input())

def solution(N):
    # A 택희 / B 영훈 / C 남규
    
    cnt = 0
    
    for a in range(2, N + 1, 2):
        for c in range(1, N + 1):
            for b in range(c + 2, N + 1):
                if a + b + c == N:
                    cnt += 1
                    
    return cnt

print(solution(N))