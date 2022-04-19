X  = int(input())
cnt = 0
if X < 10 :
    if X%3 == 0 :
        print(0)
        print("YES")
    else :
        print(0)
        print("NO")
else:
    while True : # 한자리수가 나올때까지 변환해야하므로 while문을 사용하는 것
        X_list=list(str(X)) # 정수형 리스트화하기 위한 str 사용  

        result = 0 #while문 안에 X_list와 result 넣은 이유 : X > Y로 변환할 때마다 X_list와 result를 초기화해야한다.
        for i in X_list :
            result += int(i) # i가 str때문에 문자형이 되어저 int를 사용해서 정수로 전환
        cnt += 1
        if result >= 10 : # 한 자리수가 나오기 전까지 우선 변환시킨 것을 X로 설정해서 반복
            X = result
        else : 
            if result%3 == 0 :
                print(cnt)
                print("YES")
                break    
            else : 
                print(cnt)
                print("NO")
                break