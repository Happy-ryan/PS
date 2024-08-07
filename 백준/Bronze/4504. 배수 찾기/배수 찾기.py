N = int(input())
while True:
    x = int(input())
    if x == 0:
        break
    if x % N == 0:
        print(f'{x} is a multiple of {N}.')
    else:
        print(f'{x} is NOT a multiple of {N}.')