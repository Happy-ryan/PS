t = int(input())
# 넓이의 비 = 제곱 비
for _ in range(t):
    a, b = map(int, input().split())
    print(a ** 2 // b ** 2)