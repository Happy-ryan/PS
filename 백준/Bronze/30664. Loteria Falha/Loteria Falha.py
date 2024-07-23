while True:
    x = int(input())
    if x == 0:
        break
    print('PREMIADO' if x % 42 == 0 else 'TENTE NOVAMENTE')