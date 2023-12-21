# https://www.acmicpc.net/problem/10025
n, k = map(int, input().split())
inf = 1000000
number_line = [0] * (inf + 1)

for _ in range(n):
    g, x = map(int, input().split())
    number_line[x] = g
    
init_mid = k
l, r = init_mid - k, init_mid + k
cnt = sum(number_line[: r + 1])
ans = cnt
# 시간복잡도 O(N)
for mid in range(init_mid + 1, inf - k + 1):
    # 기존의 l 삭제
    cnt -= number_line[l]
    l, r = mid - k, mid + k
    # 새로운 r 추가
    cnt += number_line[r]
    ans = max(ans, cnt)
    
print(ans)