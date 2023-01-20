import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
s = input()
conv = '0abcdefghijklmnopqrstuvwxyz'
dic = defaultdict()
for i, x in enumerate(conv):
    dic[x] = i  

res = 0

for i in range(n):
    res += dic[s[i]] * (31 ** i)

print(res)