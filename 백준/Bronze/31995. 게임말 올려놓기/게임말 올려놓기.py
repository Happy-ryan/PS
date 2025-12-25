N = int(input())
M = int(input())

def solution(N, M):
    
    if N == 1 or M == 1:
        return 0
    
    # 2x2 정사각형의안에 대각선 2개 들어있음.
    
    return (N - 1) * (M - 1) * 2
    
print(solution(N, M))