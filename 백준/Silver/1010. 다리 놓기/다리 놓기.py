T = int(input())
def factorial(x):
    if x == 0:
        return 1
    elif x == 1:
        return 1
    else:
        return x * factorial(x-1)
# print(factorial(5))
for _ in range(T):
    k,n = map(int,input().split())
    # 조합공식 : 팩토리얼 필수!
    up = factorial(n)
    down = factorial(k)*factorial(n-k)
    result = up/down
    print('{:.0f}'.format(result)) # '{:.0f}'.format 소수 첫 째자리에서 반올림