from collections import Counter

dic = Counter()

while True:
    try:
        x = input()
        for i in x:
            if i.isalpha():
                dic[i] += 1
    except:
        break
    
ans = []
max_ = max(dic.values())
for key, value in dic.items():
    if value == max_:
        ans.append(key)
ans.sort()
print(''.join(ans))