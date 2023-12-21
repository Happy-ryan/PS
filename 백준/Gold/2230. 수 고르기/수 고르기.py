# https://www.acmicpc.net/problem/2230
n, m = map(int, input().split())
numbers = [int(input()) for _ in range(n)]
# 수 쌍 > 이분탐색! && 같은 수도 고를 수 있다! 1 1 2 3 > 1, 1도 선택가능!
numbers.sort()
# 조합 > O(N^2) > 시간초과
# 이분탐색 > 무엇을 찾을까? target 지정!
# m 이상이면서 가장 작은 차이
# ex) 숫자1, m 3 > 차이가 3이상이면서 이 차이를 최소화하는 값.
# target: -2 or 4
# 이분탐색을 위해 오름차순 정렬 > 나보다 큰 target을 찾자!
# target 보다 크거나 같은 값 중 가장 작은 값!
def binary_search_smaller(idx: int, m: int):
    target = numbers[idx] + m
    l, r = idx + 1, n - 1
    ans = -1
    while l <= r:
        m = (l + r) // 2
        if numbers[m] >= target:
            r = m - 1
            ans = m
        else:
            l = m + 1
    return ans

inf = 2000000000
ans = inf + 1
for idx in range(n):
    k = binary_search_smaller(idx, m)
    if k != -1:
        ans = min(ans, abs(numbers[idx] - numbers[k]))

print(ans)