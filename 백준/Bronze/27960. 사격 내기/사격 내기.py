A, B = map(int, input().split())

def solution(A, B):
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    As = [0] * 10
    Bs = [0] * 10
    
    for i in range(10):
        k = 2 ** (nums[i])
        if A & k == k:
            As[i] = 1
        if B & k == k:
            Bs[i] = 1
    
    cnt = 0
    for i in range(10):
        k = 2 ** (nums[i])
        if (As[i] == 0 and Bs[i] == 0) or (As[i] == 1 and Bs[i] == 1):
            continue
        if (As[i] == 1 and Bs[i] == 0) or (As[i] ==0 and Bs[i] == 1):
            cnt += k
            
    return cnt
    
    
print(solution(A, B))