from collections import Counter
k, l = map(int, input().split())
lis = [ input() for _ in range(l)]
dic = Counter()
for num in lis:
    if dic[num] == 1:
        del dic[num]
        dic[num] += 1
    else:
        dic[num] += 1
# print('-------')
check = 0
for key, value in dic.items():
    if check == k:
        break
    else:
        print(key)
        check += value