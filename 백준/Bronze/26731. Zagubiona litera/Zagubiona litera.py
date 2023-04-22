# https://www.acmicpc.net/problem/26731
s = input()

check = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for x in check:
    if x not in s:
        print(x)
        break