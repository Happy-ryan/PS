n, k = map(int, input().split())
scores = [int(input()) for _ in range(k)]

def solution(n, k, scores):
    
    
    val = sum(scores)
    
    min_val = -3 * (n - k)
    max_val =  3 * (n - k)
    
    return f"{((min_val + val) / n)} {((max_val + val) / n)}"
    
    
print(solution(n, k, scores))