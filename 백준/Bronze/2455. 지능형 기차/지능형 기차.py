arr = [ input().split() for _ in range(4)]
cnt=0
result=[] # 역에 내리고 탄 후의 기차에 남아있는 승객의 수
for i in range(4):
    cnt += int(arr[i][1])
    cnt -= int(arr[i][0])
    result.append(cnt)
print(max(result))