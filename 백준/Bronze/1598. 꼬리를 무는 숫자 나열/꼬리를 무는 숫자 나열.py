arr = list(map(int, input().split()))
# # 행 : 4로 나누었을 때 나머지의 영역
# # 열 : 4로 나누었을 때 몫의 영역

# arr[0] 의 행과 열 찾기
arr0_i,arr0_j=0,0
if arr[0]%4 ==0:
    arr0_i = 4
else: arr0_i += arr[0]%4

if arr[0]%4 != 0:
    arr0_j += ((arr[0]//4) +1)
else: arr0_j += arr[0]//4
# arr[1] 의 행과 열 찾기
arr1_i,arr1_j=0,0
if arr[1]%4 ==0:
    arr1_i = 4
else: arr1_i += arr[1]%4
if arr[1]%4 != 0:
    arr1_j += ((arr[1]//4) +1)
else: arr1_j += arr[1]//4

# print(arr0_i,arr0_j)
# print(arr1_i,arr1_j)
print(abs(arr0_i-arr1_i)+abs(arr0_j-arr1_j))