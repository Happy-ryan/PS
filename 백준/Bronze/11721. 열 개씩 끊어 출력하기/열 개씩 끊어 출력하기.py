s = input()
arr= list(s)
#print(len(arr))
arr_list = [ None for _ in range(114)]    
for i in range(len(arr)) :
    arr_list[i] = arr[i]
#print(arr_list)
for x in range(11) :
    result = []
    for y in range(10*x, 10*x+10) :
        if arr_list[y] != None :
            result.append(arr_list[y])
    if result == [] :
        break    
    else :
        print(*result,sep="") # sep="" 공백제거출력