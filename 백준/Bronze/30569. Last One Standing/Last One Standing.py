import math

h1, d1, t1 = map(int, input().split())
h2, d2, t2 = map(int, input().split())

k1 = math.ceil(h2 / d1) 
k2 = math.ceil(h1 / d2) 

# 죽는 시간
time1 = (k1 - 1) * t1 + 0.5
time2 = (k2 - 1) * t2 + 0.5

if time1 < time2:
    print("player one")
elif time2 < time1:
    print("player two")
else:
    print("draw")
