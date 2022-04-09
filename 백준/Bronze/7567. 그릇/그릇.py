s = input()
list_s = list(s)
ret = 10
for i in range(len(list_s)-1) :
    if list_s[i] == list_s[i+1] :
        ret += 5
    else :
        ret += 10
print(ret)