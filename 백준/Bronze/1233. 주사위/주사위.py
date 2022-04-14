s1, s2, s3=map(int, input().split())
arr=[]
for i in range(1,s1+1) :
    sum=0 # j문을 벗어나서 sum=0으로 만들지 않으면 j문의 sum의 i가 남아있는 상태가 되므로 반드시 초기화
    sum += i
    for j in range(1, s2+1) :
        sum += j
        arr.append(sum)
        sum = i # sum을 i로 유지해야 i가 고정된 상태에서j만 더한 합의 경우가 도출된다.
#print(arr) 주사위 2개의 경우의 수 전체 총합
brr=[]
for x in arr :
    for y in range(1, s3+1) :
        result = x + y
        brr.append(result)
#print(brr) # 주사위2개의 합 조합 구한 후 주사위 1개 합 구하기
crr = list(set(brr))
#print(crr) # 중복 제거 리스트
drr =[0] * len(crr)
for k in range(len(crr)) :
    for z in range(len(brr)) :
        if crr[k] == brr[z] :
            drr[k] += 1
#print(drr) # 문자열 빈칸을 활용해서 만날 때마다 카운트 세기
result = drr.index(max(drr)) # 가장 많이 만나는 수 인덱스 찾기 > 중복이 될 경우 가장 처음에 나온 인덱스가 출력
                             # 문제에서 중복되면 가장 작은 수를 출력하기로 했으므로 max사용해도 괜찮다.
print(crr[result])