
def solution(A, B):
    
    A = '0' * (max(len(A), len(B)) - len(A)) + A
    B = '0' * (max(len(A), len(B)) - len(B)) + B
    
    L = len(A)
    
    cnt = 0
    carry = 0
    for i in range(L - 1, -1, -1):
        if int(A[i]) + int(B[i]) + carry >= 10:
            cnt += 1
            carry = 1
        else:
            carry = 0
            
    return cnt

while True:
    A, B = input().split()
    if A == '0' and B == '0':
        break
    print(solution(A, B))