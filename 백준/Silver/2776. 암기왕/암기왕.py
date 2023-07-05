# https://www.acmicpc.net/problem/2776
from collections import Counter

def solution(note1: list, note2: list):
    dic = Counter(note1)
    ans = []
    for num in note2:
        if num in dic.keys():
            ans.append(1)
        else:
            ans.append(0)
    return ans

t = int(input())

for _ in range(t):
    n1 = int(input())
    note1 = list(map(int, input().split()))
    n2 = int(input())
    note2 = list(map(int, input().split()))
    ans = solution(note1, note2)
    for x in ans:
        print(x)
    