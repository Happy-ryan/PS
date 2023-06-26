# https://www.acmicpc.net/problem/2729

def f(num1: str, num2: str):
    num1 = int(num1, 2)
    num2 = int(num2, 2)
    num = num1 + num2
    return bin(num)[2:]
t = int(input())
for _ in range(t):
    a, b = input().split()
    print(f(a, b))
