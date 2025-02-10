while True:
    x = input()
    sum_val = 0
    if x == '#':
        break
    else:
        for idx, val in enumerate(x):
            if val != ' ':
                sum_val += (idx + 1) * (ord(val) - 64)
        print(sum_val)