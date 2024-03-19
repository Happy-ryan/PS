nums = list(map(int, input().split()))
total = 5000
price = {1: 500, 2: 800, 3: 1000}
for num in nums:
    total -= price[num]
print(total)