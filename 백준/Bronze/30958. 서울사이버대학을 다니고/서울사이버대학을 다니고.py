n = int(input())
s = input()

from collections import Counter

dic = Counter(s)

ans = 0
for key, value in dic.items():
    if key.isalpha():
        ans = max(ans, value)
        
print(ans)