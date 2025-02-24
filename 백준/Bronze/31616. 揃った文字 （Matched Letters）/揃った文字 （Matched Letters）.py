n = int(input())
s = input()
a = s[0]
flag = True
for x in s[1:]:
    if x != a:
        flag = False

if flag:
    print('Yes')
else:
    print('No')