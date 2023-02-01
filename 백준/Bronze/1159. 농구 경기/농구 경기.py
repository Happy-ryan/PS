from collections import Counter

t = int(input())
dic = Counter()
for _ in range(t):
    dic[input()[0]] += 1

ans = []
for key, value in dic.items():
    if value >= 5:
        ans.append(key)

if len(ans) == 0:
    print('PREDAJA')
else:
    ans.sort()
    print(''.join(ans))