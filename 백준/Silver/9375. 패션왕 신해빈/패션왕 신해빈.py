# 해시, 수학(경우의 수)
# (x + 1)(y + 1)... - 1
from collections import Counter

n = int(input())

for _ in range(n):
    num = int(input())
    dic = Counter()
    for _ in range(num):
        name, cl = input().split()
        dic[cl] += 1
    sum = 1
    for value in dic.values():
        sum *= value + 1

    print(sum - 1)
