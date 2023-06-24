# https://www.acmicpc.net/problem/25192
from collections import Counter

n = int(input())
chats = [input() for _ in range(n)]
sum_val = 0
dic = Counter()
for chat in chats:
    if chat == "ENTER":
        sum_val += len(dic.keys())
        dic = Counter()
    else:
        dic[chat] += 1
sum_val += len(dic.keys())
print(sum_val)