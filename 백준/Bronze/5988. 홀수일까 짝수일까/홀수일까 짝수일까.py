n = int(input())
# 마지막 일의 자리 숫자만 뽑아 내고 짝함수 판단
def f(n):
    result = n%10
    if result%2 == 0:
        return "even"
    else: return "odd"

for _ in range(n):
    print(f(int(input())))