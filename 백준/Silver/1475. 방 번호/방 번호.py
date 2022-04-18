from math import ceil

N = int(input())
arr1 = [0] * 10
for i in str(N) : # 숫자를 문자열로 만들어서 포문 사용하기
    arr1[int(i)] += 1 #문자열로 만들었기 때문에 int로 정수형으로 만들고 arr사용해서 각 자리에 넣을 갯수 세기
#print(arr1)
arr2 =[]
for j in [0,1,2,3,4,5,7,8] : # 이 문제는 6,9가 같은 취급 받는다. 따라서 6,9가 없다면 나머지 숫자의 갯수에 따라서 세트가 필요하다

    arr2.append(arr1[j]) # 6,9가 존재할 수 있기 때문에 우선 인덱스6,9의 숫자와 나머지를 분류해서 나머지 중 최고 숫자를 찾아낸다.
#print(arr2)
result1 = max(arr2) # 6,9 인덱스 제외하고 최고 숫자 = 세트의 수 (후보1)
#print(result1)
result2 = ceil((arr1[6]+arr1[9])/2) # 6,9는 같은 존재이기 때문에 6669 는 2개의 세트이다. 즉 6과9의 합을 2로 나누고 반올림한 값이 세트수(후보2)
#print(result2)
if result1 >= result2 :
    print(result1)
else :
    print(result2)