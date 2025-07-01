A, B, C, D = map(int, input().split())
P, M, N = map(int, input().split())

def solution(A, B, C, D, P, M, N):
    mod1, mod2 = A + B, C + D
    dog1 = [0] * (mod1 + 1)
    dog2 = [0] * (mod2 + 1)
    
    for i in range(1, A + 1):
        dog1[i] = 1
    
    for i in range(1, C + 1):
        dog2[i] = 1
        
    
    def cal(num):
        
        cnt1 = dog1[num % mod1 if num % mod1 != 0 else mod1]
        cnt2 = dog2[num % mod2 if num % mod2 != 0 else mod2]
        return cnt1 + cnt2
    
    print(cal(P))
    print(cal(M))
    print(cal(N))

solution(A, B, C, D, P, M, N)