# https://www.acmicpc.net/problem/4447
from collections import Counter

def check(arr):
    dic = Counter(arr.lower())
    if dic['g'] > dic['b']:
        return f"{arr} is GOOD"
    elif dic['g'] < dic['b']:
        return f"{arr} is A BADDY"
    else:
        return f"{arr} is NEUTRAL"
    
t = int(input())
for _ in range(t):
    s = input()
    print(check(s))