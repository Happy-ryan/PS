s = input()
alpha = "abcdefghijklmnopqrstuvwxyz"
for x in alpha :
    if x in s :
        a = s.index(x)
        print(a)
    else :
        print(-1)