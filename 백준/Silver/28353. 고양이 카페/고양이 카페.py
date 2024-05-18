n, k = map(int, input().split())
weights = list(map(int, input().split()))

def solution(n, k, weights):
    # 정렬해도 상관없음
    weights.sort()
    # 2 4 8 11 16
    # 행복해질 수 있는 사람의 수의 최댓값 > 그리디
    # 2 4 / 8 11 / 16 - 2명
    # 2 16 / 4 11 / 8 - 2명
    # 3 4 5 6 7 9
    # 3 7 / 4 6 - 2명
    # 3 4 - 1명
    # l 고정, r이동 > r 반대로 이동하는 투포인터
    # print(weights)
    cnt = 0
    r = n - 1
    for l in range(n):
        while l < r and weights[l] + weights[r] > k:
            r -= 1
        
        if l < r and weights[l] + weights[r] <= k:
            cnt += 1
            
        r -= 1
            
    return cnt

print(solution(n, k, weights))