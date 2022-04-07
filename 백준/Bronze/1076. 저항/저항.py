s1 = input()
s2 = input() # 한줄씩 입력을 해야하므로 포문을 사용해버리면 각 색에 맞는 값과 곱셉을 찾기 어렵기 때문에
                # 각각 입력하도록 한다.
s3 = input()
arr = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
for i in arr :
    if s1 == i :
        num1 = arr.index(i) # 색과 값의 관계를 보면 색의 값이 곧 인덱스임을 알고 접근한다.
        break
for i in arr :
    if s2 == i :
        num2 = arr.index(i)
        break
for k in arr :
    if s3 == k :
        num3 = 10**(arr.index(k))
        break
print((num1*num3*10)+(num2*num3))