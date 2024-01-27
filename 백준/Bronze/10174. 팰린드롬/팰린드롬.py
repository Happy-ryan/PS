# https://www.acmicpc.net/problem/17952

def is_palin(s: str):
    s = s.lower()
    for i in range(0, len(s)//2):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True

n = int(input())

for _ in range(n):
    s = input()
    if is_palin(s):
        print("Yes")
    else:
        print("No")
