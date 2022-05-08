N = int(input())
arr = [ input() for _ in range(N)]
arr = sorted(arr)
checked_num = {}
for i in arr :
    checked_num[i] = 0
# print(checked_num)
for x in arr :
    if x in arr :
        checked_num[x] += 1
# print(checked_num)
max_key = max(checked_num, key=checked_num.get)
print(max_key)