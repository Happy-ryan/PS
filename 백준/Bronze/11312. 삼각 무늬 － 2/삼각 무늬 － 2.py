T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    k = a // b
    print(k * k)