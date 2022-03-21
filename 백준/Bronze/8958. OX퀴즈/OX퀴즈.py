n = int(input())
for _ in range(n) :
    arr = input()
    sum1 = 0
    sum2 = 0
    for j in range(len(arr)) :
        if arr[j] == "O" :
            sum1 += +1 # 1+2+3 하는 방법 : j를 써버리면 반복문 돌면서 숫자가 커져서 1+2+3 처럼 순차적 더하기가 안된다.
            sum2 += sum1 # 따라서 1+2+3과 같은 순차적 더하기 하기 위해서는 변수 두 개 사용하여 
                         # 한 변수는 +1씩 증가시키고 그 변수를 새로운 변수가 받으면 순차적 더하기가 된다.
        elif arr[j] == "X" :
            sum1 = 0
    print(sum2)
