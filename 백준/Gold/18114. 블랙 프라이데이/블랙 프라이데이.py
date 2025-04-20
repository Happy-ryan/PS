n, c = map(int, input().split())
weights = list(map(int, input().split()))

def solution(n, c, weights):
    # 정렬해도 노상관.
    weights.sort()
    # 선택가능한 물건은 최대 3개.
    # 투포인터를 n번 돌리면 맞지 않을까?
    
    def two_pointer(weights, w):
        
        # 하나 조합으로 끝날 수 있음.
        if w == c:
            return 1

        r = len(weights) - 1
        for l in range(len(weights)):
            while l + 1 < r and w + weights[l] + weights[r] > c:
                r -= 1
                
            if l != r and weights[l] + weights[r] + w == c:
                return 1
            
        
        return 0
    
    # 3개의 조합이 아닌 2개의 조합으로도 끝날 수 있다.
    if two_pointer(weights, 0):
        return 1
    
    for s in range(n):
        ans = two_pointer(weights[:s] + weights[s + 1:], weights[s])
        if ans:
            return 1
    return 0

print(solution(n, c, weights))