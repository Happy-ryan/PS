N = int(input())
arr = [ input() for _ in range(N)]
cnt1, cnt2 = 0, 0
for i in range(len(arr)):
    brr=arr[i].split("X") # "X" 를 기준으로 split 를 이용해서 쪼갠 새로운 리스트 brr
    for row in brr:
        if len(row) >=2 :
            cnt1 +=1
# print(cnt1)
for j in range(N): # 세로를 가로로 바꿔서 풀어야 한다.
    row = "" # append를 이용하면 하나의 요소씩 들어가기 때문에 문자열 더하기를 이용한다.
    for i in range(N):
        row += arr[i][j]
    crr = row.split("X")
    for x in crr:
        if len(x) >= 2:
            cnt2+=1
    #print(row) 열 > 행으로 변환
print(cnt1,cnt2) 
 