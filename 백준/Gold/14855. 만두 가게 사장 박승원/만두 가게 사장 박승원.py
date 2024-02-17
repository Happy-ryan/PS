# https://www.acmicpc.net/problem/14855
# item: 만두 / weight: 밀가루 / value: 값어치
# 보석(item)의 무게(weight), 가치(value) 가방 문제와 동일함. 
# 다만 여기는 각 만두를 만들 수 있는 만두속은 '전용 만두속'이므로 예를 들어 1번 만두가 2개 있을 수도 있고 2번 만두는 3개 있을 수도 있다.
# 보석 문제와 동일하게 풀고 싶어서 나는 각 만두를 다른 만두로 생각하고 mandos_in라는 곳에 하나씩 담았다.

# 따라서, 이 문제의 핵심은 밀가루 라는 공공재를 어떻게 사용해서 최대 이익을 창출할 수 있는가에 대한 물음이다.

n, m, c0, d0 = map(int, input().split())
infos = [list(map(int, input().split())) for _ in range(m)]

mandos_in = [0]
mando_cnt = 0
for a1, b1, c1, d1 in infos:
    mando_cnt += a1//b1
    for _ in range(a1 // b1):
        mandos_in.append((c1, d1))

inf = int(1e9)
k = len(mandos_in)
dp = [[-inf for _ in range(n + 1)] for _ in range(k + 1)]

dp[0][0] = 0
# i번째 만두(itwm)를 선택해서  밀가루j(weight)를 만들었을 때의 값어치(value)!
for i in range(1, k):
    w, v = mandos_in[i]
    # 만두 중복 사용 불가 > 반대로 봐야함!
    for j in range(n, -1, -1):
        dp[i][j] = dp[i - 1][j]
        if j - w >= 0:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - w] + v)

for w, v in [(c0, d0)]:
    for j in range(1, n + 1):
        if w <= j:
            dp[k-1][j] = max(dp[k-1][j], dp[k - 1][j - w] + v)
            
print(max(dp[k-1]))