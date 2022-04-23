arr = [list(map(int,input().split())) for _ in range(10)] # input을 이미 list했기 때문에 또 감쌀 필요는 없다
#brr = [[ 0 for _ in range(5)] for _ in range(5)]
#print(brr) #5x5행렬 생성
cnt = 0
result=[]
for i in range(5,10) :
    for j in range(0,5) :
        call_num = arr[i][j]
        cnt += 1
        ret = 0
        for x in range(5) :
            for y in range(5) :
                if arr[x][y] == call_num :
                    arr[x][y] = 0
        if arr[0][0]+ arr[0][1]+ arr[0][2]+ arr[0][3]+ arr[0][4] == 0 :
            ret +=1
        if arr[1][0]+ arr[1][1]+ arr[1][2]+ arr[1][3]+ arr[1][4] == 0 :
            ret +=1
        if arr[2][0]+ arr[2][1]+ arr[2][2]+ arr[2][3]+ arr[2][4] == 0 :
            ret +=1
        if arr[3][0]+ arr[3][1]+ arr[3][2]+ arr[3][3]+ arr[3][4] == 0 :
            ret +=1
        if arr[4][0]+ arr[4][1]+ arr[4][2]+ arr[4][3]+ arr[4][4] ==0 :
            ret +=1
        if arr[0][0]+ arr[1][0]+ arr[2][0]+ arr[3][0]+ arr[4][0] ==0 :
            ret +=1
        if arr[0][1]+ arr[1][1]+ arr[2][1]+ arr[3][1]+ arr[4][1] ==0:
            ret +=1
        if arr[0][2]+ arr[1][2]+ arr[2][2]+ arr[3][2]+ arr[4][2] ==0 :
            ret +=1
        if arr[0][3]+ arr[1][3]+ arr[2][3]+ arr[3][3]+ arr[4][3] ==0 :
            ret +=1
        if arr[0][4]+ arr[1][4]+ arr[2][4]+ arr[3][4]+ arr[4][4] ==0 :
            ret +=1
        if arr[0][0]+ arr[1][1]+ arr[2][2]+ arr[3][3]+ arr[4][4] ==0 :
            ret +=1
        if arr[0][4]+ arr[1][3]+ arr[2][2]+ arr[3][1]+ arr[4][0] ==0 :
            ret +=1
        if ret >=3 :
            result.append(cnt)
print(min(result))
