s = input()
sum = 0
for i in s :
    if i in "ABC" :
        sum +=3
    elif i in "DEF" :
        sum +=4
    elif i in "GHI" :
        sum +=5
    elif i in "JKL" :
        sum +=6
    elif i in "MNO" :
        sum +=7
    elif i in "PQRS" :
        sum +=8
    elif i in "TUV" :
        sum +=9
    elif i in "WXYZ" :
        sum +=10
print(sum)