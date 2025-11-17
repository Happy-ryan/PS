n = int(input())

prices = [float(input()) for _ in range(n)]
prices.sort()

print(f"{prices[1]:.2f}")