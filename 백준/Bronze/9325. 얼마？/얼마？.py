t = int(input())

for _ in range(t):
    price = 0
    s = int(input())
    
    n = int(input())
    for _ in range(n):
        p, q = map(int, input().split())
        price += p * q
    price += s
    
    print(price)