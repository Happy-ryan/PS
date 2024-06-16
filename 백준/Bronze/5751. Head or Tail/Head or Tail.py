while True:
    n = int(input())
    if n == 0:
        break
    numbers = list(map(int, input().split()))
    print(f'Mary won {numbers.count(0)} times and John won {numbers.count(1)} times')