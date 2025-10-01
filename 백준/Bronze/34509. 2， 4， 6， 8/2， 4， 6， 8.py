for x in range(10, 100):
    s_x = str(x)
    sum_x = int(s_x[0]) + int(s_x[1])
    r_x = int(s_x[::-1])
    if r_x % 4 == 0 and sum_x % 6 == 0 and '8' not in s_x:
        print(x)
        break