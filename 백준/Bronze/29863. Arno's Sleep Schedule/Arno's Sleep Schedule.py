sleep = int(input())
wake = int(input())
if 20 <= sleep and sleep <= 23:
    print(wake + 24 - sleep)
else:
    print(wake - sleep)