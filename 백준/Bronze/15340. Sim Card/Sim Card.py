while True:
    c, d = map(int, input().split())
    if c == 0 and d == 0:
        break
    
    c1 = 30 * c + 40 * d
    c2 = 35 * c + 30 * d
    c3 = 40 * c + 20 * d
    
    print(min(c1, c2, c3))