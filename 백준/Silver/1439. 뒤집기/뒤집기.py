arr = input()
s,e = 0,0
result = []
while e != len(arr):
    if arr[s] == arr[e]:
        e += 1
    else:
        result.append(arr[s:e])
        s = e
result.append(arr[s:e]) #while문으로 나눌 수 없는 마지막 파트는 s,e를 이용해서 따로 append하기
# print(result) #1~9line : 000 11 00 을 덩어리째로 구분하기 위함.
cnt_0 = 0
cnt_1 = 0
for row in result:
    if '0' in row:
        cnt_0 +=1
    else: cnt_1 +=1
# print(cnt_0)
# print(cnt_1)
print(min(cnt_0,cnt_1))