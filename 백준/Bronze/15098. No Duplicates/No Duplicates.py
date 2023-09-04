from collections import Counter;

s = input().split()
dic = Counter(s)
flag = False
for value in dic.values():
    if value >= 2:
        flag = True

print("no" if flag else "yes")