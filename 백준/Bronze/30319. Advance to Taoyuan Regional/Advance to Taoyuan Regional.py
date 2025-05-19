y, m, d = map(int, input().split('-'))


if y > 2023:
    print('TOO LATE')
elif y == 2023:
    if m > 9:
        print('TOO LATE')
    elif m == 9:
        if d > 16:
            print('TOO LATE')
        else:
            print("GOOD")
    else:
        print("GOOD")
else:
    print("GOOD")