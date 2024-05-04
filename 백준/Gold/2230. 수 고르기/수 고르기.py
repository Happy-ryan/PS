n, m = map(int, input().split())
A = [int(input()) for _ in range(n)]

def solution(n, m, A):
    # 두 수를 골랐을 때 (같은 수 포함) / 그 차이가 m 이상이면서 제일 작은 경우
    
    # 정렬해도 상관없음!
    # 투포인터 문제는 대부분 이분탐색으로 풀린다.
    A.sort()
    # 투포인터 l과 r이 있을 때, l과 r 한 방향으로만 이동할 때!!
    # 이분탐색 - 쌍을 구할 때는 하나를 고정하고!!
    def two_pointer(n, m):
        
        r = 1
        ans = int(1e18)
        for l in range(0, n):
            while r + 1 < n and (A[r] - A[l] < m or l == r) :
                r += 1
                
            if A[r] - A[l] >= m:
                ans = min(ans, A[r] - A[l])
        
        return ans
    
    return two_pointer(n, m)


print(solution(n, m, A))