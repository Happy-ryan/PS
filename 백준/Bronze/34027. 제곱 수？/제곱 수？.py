t = int(input())

for _ in range(t):
    n = int(input())
    
    if int(n ** 0.5) * int(n ** 0.5) == n:
        print(1)
    else:
        print(0)