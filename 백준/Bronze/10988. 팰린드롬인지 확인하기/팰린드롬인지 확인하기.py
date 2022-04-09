s = input()
list_s = list(s)
long = len(list_s)
cnt = 0
for i in range(long//2) :
    if  list_s[i]==list_s[len(list_s)-i-1] :
        cnt += 1    
    else :
        print(0)
        break
if cnt == long//2 :
    print(1)   