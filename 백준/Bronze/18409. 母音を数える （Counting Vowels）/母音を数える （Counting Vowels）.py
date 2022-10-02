N = int(input())
s = list(input())
arr = ['a','i','u','e','o']
cnt = 0
for k in s:
    if k in arr:
        cnt += 1
print(cnt)