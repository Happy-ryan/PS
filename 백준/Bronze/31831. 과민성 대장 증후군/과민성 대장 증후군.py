N, M = map(int, input().split())
A = list(map(int, input().split()))

def solution(N, M, A):
    psum = [0] * (N + 1)
    cnt = 0
    for i in range(N):
        psum[i + 1] = max(0, psum[i] + A[i])
        if psum[i + 1] >= M:
            cnt += 1
    
    # print(psum)
    
    return cnt

print(solution(N, M, A))