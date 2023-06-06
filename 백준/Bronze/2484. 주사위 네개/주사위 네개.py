# https://www.acmicpc.net/problem/2484

def solution(arr: list):
    if len(set(arr)) == 1:
        return 50000 + arr[0] * 5000
    elif len(set(arr)) == 4:
        return 100 * max(arr)
    elif len(set(arr)) == 2:
        flag = True
        for x in arr:
            if arr.count(x) == 3:
                flag = False
        if flag:
            return 2000 + 500 * (min(arr) + max(arr))
        else:
            return 10000 + x * 1000
    else:
        for x in arr:
            if arr.count(x) == 2:
                return 1000 + x * 100
            
t = int(input())
max_money = 0
for _ in range(t):
    arr = list(map(int, input().split()))
    max_money = max(max_money, solution(arr))

print(max_money)