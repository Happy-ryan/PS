from collections import Counter
n, c = map(int, input().split())
arr = list(map(int, input().split()))
dic = Counter(arr)

check = set()
res = []
for x in arr:
    if x not in check:
        check.add(x)
        res.append(x)
# print(dic)
# print(res)

ans = []
for i, x in enumerate(res):
    ans.append((dic[x], i, x))
    
# 정렬 기준 : 1. 빈도수(내림차순 - 리버스)  - > 2. 인덱스(올림차순 - 기본)
# 두 번 정렬할 때는 1 - > 2 : 2조건 먼저 기록 후 1조건 기록
ans.sort( key = lambda x : x[1]) 
ans.sort( key = lambda x : x[0], reverse= True)

for fre, idx, val in ans:
    for _ in range(fre):
        print(val, end = ' ')