n = int(input())

prices = [350.34, 230.9, 190.55, 125.3, 180.9]

for _ in range(n):
    cnts = list(map(int, input().split()))
    val = 0
    for i in range(5):
        val += prices[i] * cnts[i]
    
    print(f"${val:.2f}")