n, m, k = map(int, input().split())

jump = 1
cnt = 0

dog = 0
rabbit = n
while True:
    if dog >= rabbit:
        print(cnt)
        break
    dog += jump * k
    rabbit += jump * m
    cnt += 1