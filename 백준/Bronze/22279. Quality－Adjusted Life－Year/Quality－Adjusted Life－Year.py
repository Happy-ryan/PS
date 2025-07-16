n = int(input())
arr = [list(map(float, input().split())) for _ in range(n)]

def solution(arr):
    
    val = 0
    
    for row in arr:
        q, y = row
        val += q * y
        
    return val

print(solution(arr))