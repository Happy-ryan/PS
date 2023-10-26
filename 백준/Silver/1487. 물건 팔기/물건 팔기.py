# https://www.acmicpc.net/problem/1487
n = int(input())
moneys = [list(map(int, input().split())) for _ in range(n)]

moneys.sort(key=lambda x: x[0])
max_pirce = moneys[-1][0]

profit = []
for price in range(1, max_pirce + 1):
    sum_val = 0
    for p, c in moneys:
        # price가 내가 지불할 최대 금액인 p보다 작야아 구매 
        # 세준이 입장에서는 손해보고 팔고 싶지는 않기 때문에 현재 가격 price보다 배송비가 더 비싸면 안팔아!
        if price <= p and price >= c :
            sum_val += (price - c)
    profit.append((price, sum_val))

# (현재가격, 이익)
# 이익 - 오름차순, 가격 - 내림차순
profit.sort(key=lambda x: (-x[1], x[0]))

if profit[0][1] == 0:
    print(0)
else:
    print(profit[0][0])