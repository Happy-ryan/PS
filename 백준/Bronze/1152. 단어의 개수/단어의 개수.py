s = input()
cnt = 0
for i in s :
    if i ==" ":
        cnt+=1
if s[0] == " " and s[len(s)-1] == " " :
    cnt -=2
    print(cnt+1)
elif s[0] == " " or s[len(s)-1]== " " :
    cnt -=1
    print(cnt+1)
else :
    print(cnt+1)