while True:
    s = int(input())
    if s == -1:
        break
    records = [list(map(int, input().split())) for _ in range(s)]
    sum_val = 0
    for idx, (v, t) in enumerate(records):
        if idx == 0:
            sum_val += v * t
            t_pre = t
        else:
            sum_val += v * (t - t_pre)
            t_pre = t
    
    print(f"{sum_val} miles")