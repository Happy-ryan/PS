t = int(input())

def solution(N, M, X, Y,  nums):
    x = int(''.join(X))
    y = int(''.join(Y))
    
    nums = nums + nums # 회전
    
    cnt = 0
    for idx in range(N):
        z = int(''.join(nums[idx : idx + M]))
        if x <= z and z <= y:
            cnt += 1
            
    return cnt

for _ in range(t):
    N, M = map(int, input().split())
    X = list(input().split())
    Y = list(input().split())
    nums = list(input().split())
    print(solution(N, M, X, Y,  nums))  