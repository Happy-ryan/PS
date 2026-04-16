h, m = map(int, input().split(":"))
N = int(input())

cnt = 0

while True:
    if m == 0:
        cnt += h
    elif m in [15, 30, 45]:
        cnt += 1
    
    if cnt >= N:
        print(f"{h:02d}:{m:02d}")
        break
    
    m += 1
    if m == 60:
        m = 0
        h += 1
        if h == 13:
            h = 1