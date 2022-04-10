cnt = 0
for i in range(8) :
    s = input()
    if i%2 == 0 :
        for j in range(0,7,2) :
            if s[j] =="F" :
                cnt += 1
    elif i%2 != 0 :
        for k in range(1,8,2) :
            if s[k] == "F" :
                cnt += 1
print(cnt)