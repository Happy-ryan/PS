scores = list(map(int, input().split()))

def solution(scores):
    max_scores  = [100, 100, 200, 200, 300, 300, 400, 400, 500]
    
    val = 0
    
    for s, max_s in zip(scores, max_scores):
        if s > max_s:
            return 'hacker'
        val += s
        
    if val >= 100:
        return 'draw'
    
    return 'none'

print(solution(scores))