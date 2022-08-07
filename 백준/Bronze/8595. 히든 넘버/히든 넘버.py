import sys

input = sys.stdin.readline
n = int(input())
s = input()

cur = 0
sum = 0
for x in s:
    if '0' <= x <= '9':
        cur = cur * 10 + int(x)
    else:
        sum += cur
        cur = 0
print(sum + cur)