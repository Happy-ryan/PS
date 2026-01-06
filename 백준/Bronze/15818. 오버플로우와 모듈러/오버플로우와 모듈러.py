n, m = map(int, input().split())
a = list(map(int, input().split()))

def solution(n, m, a):
    
    ans = 1
    for i in a:
        ans *= (i % m) # 나눌 값도 모듈러
        ans %= m # 결과값도 모듈러
        
    return ans

print(solution(n, m, a))