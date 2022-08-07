n = int(input())
s = input()

cur = 0
sum = 0
for i in range(n):
    if s[i] in "0123456789":
        cur = cur*10+ int(s[i])
    else: 
        sum += cur
        cur = 0

if s[-1] in "0123456789":
    print(sum+cur)
else:
    print(sum)