t1, m1, t2, m2 = map(int, input().split())

h1 = t1 * 60 + m1
h2 = t2 * 60 + m2

if h1 > h2:
    h2 += 24 * 60
    
t = h2 - h1

print(t, t // 30)