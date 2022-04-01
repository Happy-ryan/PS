a, b = map(int, input().split(" "))
arr_a=[]
arr_b=[]
arr_max=[]
if a==1 and b != 1:
    print(1)
    print(b)
elif a != 1 and b==1 : # a or b가 1을 가지고 있는 경우 
    print(1)
    print(a)
elif a==b :
    print(a)
    print(a)
else: 
    for x in range(2, max(a,b)+1) : # 이 부분은 7 9와 같이 공약수가 1만 있고 최소공배수는 서로 곱해야하는 경우를 표현하기 위한 for문
        check = False
        if a%x == 0 and b%x == 0 : # 2부터 둘 중 큰 수까지 차례로 나누었을 때 동시에 0이 된다는 것은 공약수가 존재한다는 의미
            check = True
            break
    if check == False :
        print(1)
        print(a*b) 
    else :            # 공약수가 존재하면 check=True로 출력되어 if(20라인)문을 거치치 않는다.
        for i in range(2, a+1) :
            if a%i == 0 :
                arr_a.append(i)
        for j in range(2, b+1):
            if b%j == 0 :
                arr_b.append(j)
        for k in range(len(arr_a)) :
            if arr_a[k] in arr_b :
                arr_max.append(arr_a[k])
        print(arr_max[-1])
        print(round((a*b)/arr_max[-1])) 
