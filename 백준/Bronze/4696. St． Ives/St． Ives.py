while True:
    n = float(input())
    ans = 1+n+n**2+n**3+n**4
    if n == 0: break
    print(f"{ans:.2f}")