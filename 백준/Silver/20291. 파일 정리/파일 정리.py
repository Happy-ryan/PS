from collections import Counter
t = int(input())
dic = Counter()

for _ in range(t):
    name, cmd = input().split('.')
    dic[cmd] += 1
    
ans = []
for key, value in dic.items():
    ans.append((key, value))
    
ans.sort( key = lambda x : x[0])

for name, num in ans:
    print(name, num)