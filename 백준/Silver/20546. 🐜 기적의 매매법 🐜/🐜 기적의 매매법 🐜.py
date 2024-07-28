money = int(input())
prices = list(map(int, input().split()))

def Junhyeon_solution(money, prices):
    final_day = 13
    stocks = [0] * 15
    for day, price in enumerate(prices):
        if money >= price:
            buy_stock = money // price
            stocks[day + 1] = buy_stock
            money -= price * buy_stock
    
    asset = money + sum(stocks) * prices[final_day]
    return asset

# 소유하고 있는 주식이 3일이상 상승하면 상승하는 마지막 3일에 반드시 매도
# 3일 연속 하락한 주식은 반드시 상승하므로 하락한 마지막 3일에 반드시 매수
# 정리하면
# >> 3일 하락 시 주식 구매
# >> 3일 증가 시 주식 판매

def Seongmin_solution(money, prices):
    
    def up_down_judge(day):
        if  prices[day - 3] < prices[day - 2] and\
            prices[day - 2] < prices[day - 1] and\
            prices[day - 1] < prices[day]:
                return "S"
        if  prices[day - 3] > prices[day - 2] and\
            prices[day - 2] > prices[day - 1] and\
            prices[day - 1] > prices[day]:
                return "B"
        return "N"
        
    asset = 0
    stocks = [0] * 15
    for day, price in enumerate(prices):
        if day >= 3:
            decision = up_down_judge(day)
            if decision == "B":
                if money >= price:
                    buy_stock = money // price
                    stocks[day + 1] = buy_stock
                    money -= price * buy_stock
            elif decision == "S":
                if sum(stocks) > 0:
                    asset += sum(stocks) * price
                    # 주식 초기화
                    stocks = [0] * 15
            # print(f"day: {day + 1}, decision: {decision}")
            # print(f"stocks: {stocks}")
            # print("=")
    asset += money
    asset += sum(stocks) * prices[13]
        
    return asset


if Junhyeon_solution(money, prices) > Seongmin_solution(money, prices):
    print("BNP")
elif Junhyeon_solution(money, prices) < Seongmin_solution(money, prices):
    print("TIMING")
else:
    print("SAMESAME")