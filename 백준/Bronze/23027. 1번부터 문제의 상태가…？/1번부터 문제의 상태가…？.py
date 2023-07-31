# https://www.acmicpc.net/problem/23027
from collections import Counter

s = input()
dic_s = Counter(s)

if dic_s['A'] != 0:
    s = s.replace('B', 'A')
    s = s.replace('C', 'A')
    s = s.replace('D', 'A')
    s = s.replace('F', 'A')
else:
    if dic_s['B'] != 0:
        s = s.replace('C', 'B')
        s = s.replace('D', 'B')
        s = s.replace('F', 'B')
    else:
        if dic_s['C'] != 0:
            s = s.replace('D', 'C')
            s = s.replace('F', 'C')
        else:
            s = 'A' * len(s)
            
print(s)