def f(s: str):
    flag = 0
    for i, x in enumerate(s):
        if i == 0:
            if abs(ord(x) - ord(s[1])) == 1:
                flag += 1
        elif i == 4:
            if abs(ord(x) - ord(s[3])) == 1:
                flag += 1
        else:
            if abs(ord(x) - ord(s[i + 1])) == 1 and abs(ord(x) - ord(s[i - 1])) == 1:
                flag += 1
    return flag


n = int(input())
s = input()
flag = False
for i in range(n - 4):
    if f(s[i : i + 5]) == 5:
        flag = True
        break

if flag:
    print("YES")
else:
    print("NO")
