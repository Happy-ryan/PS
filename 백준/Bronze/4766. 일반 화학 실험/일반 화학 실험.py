prev = -11

while True:
        n = float(input())
        
        if n == 999:
            break
        
        if prev == -11:
            prev = n
        else:
            print(f"{(n - prev):.2f}")
            prev = n