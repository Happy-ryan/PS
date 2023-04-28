# https://www.acmicpc.net/problem/7600
from collections import Counter


def solution(s:str):
    s = s.lower()
    dic = Counter()
    for x in s:
        if "a" <= x <= "z" and dic[x] == 0:
            dic[x] += 1
    return sum(dic.values())


while True:
    s = input()
    if s =="#":
        break
    print(solution(s))