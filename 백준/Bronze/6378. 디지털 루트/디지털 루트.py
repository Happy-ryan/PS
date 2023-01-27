def cal(x):
    ans = 0
    while x > 0:
        ans += x % 10 # % 10 나머지 구하는 것
        x //= 10 # 자릿수 줄이기
    return ans

while True:
    n = int(input())
    if  n == 0:
        break
    while True:
        if len(str(n)) == 1:
            print(n)
            break
        n = cal(n)