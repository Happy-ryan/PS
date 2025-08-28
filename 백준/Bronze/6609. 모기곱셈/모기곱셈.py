while True:
    try:
        m, p, l, e, r, s, n = map(int,input().split())
        
        for i in range(n):
            k = m
            m = p // s
            p = l // r
            l = k * e 
            
        print(m)
    except:
        break