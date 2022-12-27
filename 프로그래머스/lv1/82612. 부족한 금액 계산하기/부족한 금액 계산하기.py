def solution(price, money, count):
    total = price * sum(list(range(1, count + 1)))
    if total > money:
        return total - money
    else:
        return 0
