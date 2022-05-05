N = int(input())
arr=[int(input()) for _ in range(N)]
result=[]
for i in arr:
    if i !=0:
        result.append(i)
    else: result.pop(len(result)-1) # 가장 마지막 요소 pop() 시키기
sum = 0
for j in result :
    sum += j
print(sum)