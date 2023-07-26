# https://www.acmicpc.net/problem/11257

def f(arr: list):
    id = arr[0]
    S, I, T = arr[1:]
    if (S >= 35 * 0.3) and (I >= 25 * 0.3) and (T >= 40 * 0.3) and (S + T + I) >= 55:
        return f"{id} {S+T+I} PASS"
    else:
        return f"{id} {S+T+I} FAIL"
        
t = int(input())
for _ in range(t):
    arr = list(map(int, input().split()))
    print(f(arr))