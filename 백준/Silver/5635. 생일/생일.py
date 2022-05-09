T = int(input())
arr = [ input().split() for _ in range(T)]
for i in range(T):
    for j in range(i, T):
        if int(arr[i][3]) < int(arr[j][3]):
            arr[i],arr[j] = arr[j],arr[i] # 태어난 년도로 정렬한 결과
        elif int(arr[i][3]) == int(arr[j][3]):
            if int(arr[i][2]) < int(arr[j][2]):
                arr[i],arr[j] = arr[j],arr[i] # 태어난 년도 정렬 >
            elif arr[i][2] == arr[j][2]:
                if arr[i][1] < arr[j][1]:
                    arr[i],arr[j]=arr[j],arr[i]
print(arr[0][0])
print(arr[T-1][0])