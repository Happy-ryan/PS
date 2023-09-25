# https://www.acmicpc.net/contest/problem/1061/7
# 10^6
from collections import Counter

n = int(input())
arr = list(map(int, input().split()))


def f(arr: list):
    visited = [False] * len(arr)
    num_list = list(Counter(arr).items())
    num_list.sort(key=lambda x: x[0])
    for row in num_list:
        start = 1
        for idx, x in enumerate(arr):
            if x == row[0] and not visited[idx]:
                visited[idx] = True
                arr[idx] = start
                start += 1
    return arr


def g(arr:list):
    ans = []
    for x in arr:
        ret = []
        if x == 1:
            ans.append("/")
            ans.append(str(x))
        else:
            ans.append(str(x))
    return ans


def z(arr: list):
    flag = True
    for i in range(len(arr) - 1):
        if abs(int(arr[i]) - int(arr[i + 1])) >= 2:
            flag = False
            break
    return flag


ans = g(arr)
arr = "".join(ans).split("/")[1:]
ret = ""
s = 1

for row in arr:
    if z(row[1:]):
        for idx, x in enumerate(f(list(row))):
            if idx == 0 and x == 1:
                ret += str(s) + " "
                s += 1
            else:
                ret += str(x) + " "
    else:
        ret = -1
        break

if len(arr) == 1 and arr[-1] == "1":
    ret = 1
else:
    if len(arr) == 0:
        ret = -1

print(ret)