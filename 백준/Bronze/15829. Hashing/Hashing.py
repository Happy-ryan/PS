import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
s = input()
res = 0
# 아스키 코드 a : 97
for i in range(n):
    res += (ord(s[i]) - 96) * (31 ** i)

print(res % 1234567891)