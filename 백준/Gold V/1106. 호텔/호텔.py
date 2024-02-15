c, n = map(int, input().split())
# (비용, 고객 수)
infos = [list(map(int, input().split())) for _ in range(n)]

def sol_1():
    # 동전을 배수로 쓸 수 있다 > 동전을 중복해서 사용할 수 있다!!
    # 앞에서부터 보면 된다.
    # 특정 도시(item) - 고객(weight) / 비용(value)
    # 문제는 '고객'을 특정할 수 없는 상황 > 따라서 고객과 비용을 반대로 생각해야함.
    # 특정 도시(item) - 고객(value) / 비용(weight)
    # 최대비용 1000명 홍보
    # 비용100 1명
    # 비용 100 * 1000 => 1000명 홍보 가능!!
    max_cost = 100 * 1000
    # 비용i원일 때 얻는 최대 고객의 수!
    # 중복사용가능 > 1차원 > dp[i] weight를 i얻을 때 최대, 최소 value
    dp = [-1 for _ in range(max_cost + 1)]
    
    dp[0] = 0
    for w, v in infos:
        for i in range(1, max_cost + 1):
            if w <= i:
                dp[i] = max(dp[i], dp[i - w] + v)

    # idx가 곧 비용을 의미함
    min_cost = max_cost
    for idx, cus_num in enumerate(dp):
        if c <= cus_num:
            min_cost = min(min_cost, idx)
                        
    return min_cost

print(sol_1())