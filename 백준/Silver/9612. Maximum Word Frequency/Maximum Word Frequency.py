# Counter - 해쉬
from collections import Counter

n = int(input())
dic = Counter()
for _ in range(n):
    dic[input()] += 1

s = list(dic.items())
s.sort(key=lambda x: (x[1], x[0]))
print(f"{s[-1][0]} {s[-1][1]}")
