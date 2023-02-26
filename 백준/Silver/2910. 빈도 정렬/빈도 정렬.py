from collections import Counter
n, c = map(int, input().split())
arr = list(map(int, input().split()))
dic = Counter(arr)
# 정렬 기준 : 1. 빈도수(내림차순 - 리버스)  - > 2. 인덱스(올림차순 - 기본)
# Counter 함수는 인덱스 보장
ans = list(dic.items())
ans.sort( key = lambda x : x[1], reverse= True)

for val, fre in ans:
    for _ in range(fre):
        print(val, end = ' ')