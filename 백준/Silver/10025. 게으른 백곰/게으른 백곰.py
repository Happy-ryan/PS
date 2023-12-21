# https://www.acmicpc.net/problem/10025
n, k = map(int, input().split())
inf = 1000000
number_line = [0] * (inf + 1)

for _ in range(n):
    g, x = map(int, input().split())
    number_line[x] = g
# 좌표가 0base임.
init_mid = k
l, r = init_mid - k, init_mid + k
cnt = sum(number_line[: r + 1])
ans = cnt
# 시간복잡도 O(N)
# 마지막 범위 주의하기! (ex) k = 3 / inf - 3, inf -2, inf - 1, inf
# inf - 3까지 와야함, +1 안하면 inf - 4가 마지막 범위임.
for mid in range(init_mid + 1, inf - k + 1):
    # 기존의 l 삭제
    cnt -= number_line[l]
    l, r = mid - k, mid + k
    # 새로운 r 추가
    cnt += number_line[r]
    ans = max(ans, cnt)
    
print(ans)