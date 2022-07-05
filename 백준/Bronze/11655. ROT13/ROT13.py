s = list(input())
for i in range(len(s)):
    if s[i]==' ':
        pass
    elif s[i] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz':
        if s[i] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            aski = ord(s[i])
            if (aski + 13) > 90:
                s[i] = chr(aski+13-26)
            else:
                s[i] = chr(aski +13)
        else:
            aski = ord(s[i])
            if (aski + 13) > 122:
                s[i] = chr(aski + 13 -26)
            else:
                s[i] = chr(aski + 13)
    else: pass

for x in s:
    print(x,end="")
