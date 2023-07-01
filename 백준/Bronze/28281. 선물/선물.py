n, x = map(int, input().split())
prices = list(map(int, input().split()))
sum_val = int(1e18)

for i in range(n - 1):
    sum_val = min( x * (prices[i] + prices[i + 1]), sum_val)
    
print(sum_val)