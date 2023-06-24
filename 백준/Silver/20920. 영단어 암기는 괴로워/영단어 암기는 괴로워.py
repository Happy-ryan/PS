# https://www.acmicpc.net/problem/20920
from collections import Counter

n, m = map(int, input().split())
dic = Counter()
for _ in range(n):
    word = input()
    dic[word] += 1
    
ans = list(dic.items())
# sort를 하나씩 쓸 경우 우선순위랑 반대로..
ans.sort(key=lambda x: x[0])
ans.sort(key=lambda x: len(x[0]), reverse=True)
ans.sort(key=lambda x: x[1], reverse=True)
for row in ans:
    if len(row[0]) >= m:
        print(row[0])
