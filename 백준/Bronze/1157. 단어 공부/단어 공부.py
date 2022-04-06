S = input().upper()
T = list(set(S))
cnt = [0] * len(T)
for s in S:
    for i in range(len(T)):
        if s == T[i]:
            cnt[i] += 1
x = max(cnt)
ret = 0

for i in cnt : 
    if i == x :
        ret +=1
if ret >=2 :
    print("?")
else :
    result = cnt.index(x)
    print(T[result])