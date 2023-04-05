# https://www.acmicpc.net/problem/27160

from collections import Counter

t = int(input())
dic = Counter()
for _ in range(t):
    s, num = input().split()
    num = int(num)
    dic[s] += num

flag = "NO"
for value in dic.values():
    if value == 5:
        flag = "YES"
        
print(flag)
        

        
    