# https://www.acmicpc.net/problem/9085

def f(arr):
    return sum(arr)

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(f(arr))