t = int(input())

def solution(n, k, candies):
    
    cnt = 0
    
    for c in candies:
        cnt += c // k
        
    return cnt

for _ in range(t):
    n, k = map(int, input().split())
    candies = list(map(int, input().split()))
    print(solution(n, k, candies))