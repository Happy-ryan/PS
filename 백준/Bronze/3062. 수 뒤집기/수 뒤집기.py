T = int(input())
for _ in range(T) :
    result = 0
    n = int(input())
    n_list = list(str(n))
    #print(n_list)
    n_list_rever=n_list[::-1] # 문자열 역순
    n_reverse= "".join(n_list_rever)
    result = n + int(n_reverse)
    #print(result) # 역순까지 더한 값
    #print(list(str(result))) #역순더한 값을 문자열로 전환하고 리스트화하기
    arr=list(str(result)) 
    if arr == arr[::-1] : # 좌우대칭이 되면 역순으로 문자열한 것과 동일함
        print("YES")
    else :
        print("NO")