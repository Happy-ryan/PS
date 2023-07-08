# https://www.acmicpc.net/problem/16499
from collections import Counter

n = int(input())
dic = Counter()
for _ in range(n):
    word = sorted(list(input()))
    word = ''.join(word)
    dic[word] += 1
    
print(len(dic.keys()))