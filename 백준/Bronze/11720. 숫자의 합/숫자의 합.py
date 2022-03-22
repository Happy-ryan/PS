n = int(input())
arr = input()
sum = 0
for i in range(n) :
    sum = sum + int(arr[i]) #인덱스할 때 반드시 범위 체크하기
print(sum)