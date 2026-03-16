n = int(input())
s = input()

from collections import Counter

dic = Counter(s)

print(min(dic['u'], dic['o'], dic['s'], dic['p'], dic['c']))