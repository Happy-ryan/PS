n, m = map(int, input().split())
a = [int(input()) for _ in range(n)]
a.sort()


def solution(n, m, a):
    r = 0
    ans = int(1e18)
    for l in range(0, n): # l을 고정
        while r + 1 < n and (l == r or a[r] - a[l] < m): 
            r += 1
        if l != r and a[r] - a[l] >= m:
            ans = min(ans, a[r] - a[l])
    return ans
            
print(solution(n, m, a))