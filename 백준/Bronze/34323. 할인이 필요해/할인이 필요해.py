N, M, S = map(int, input().split())

def solution(N, M, S):
    # 할인 no
    A = (M + 1) * S * (100 - N) // 100
    # 할인
    B = M * S
    
    return min(A, B)

print(solution(N, M, S))