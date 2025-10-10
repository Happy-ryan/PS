N = int(input())
W = int(input())
    
def solution(N, W):
    score = N * 10
    
    if N >= 3:
        score += 20
    if N == 5:
        score += 50
    if W > 1000:
        score -= 15
    return max(0, score)

print(solution(N, W))