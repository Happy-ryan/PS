arr =[ input() for _ in range(5)]
for j in range(15) : # 열을 먼저 읽기 때문에 열(j)부터 인식하기
    for i in range(5) : # 5행은 반드시 존재 
        if j < len(arr[i]) : # 열에 빠지는 숫자가 존재한다. 해당 행의 길이보다 큰 열은 존재하지 않는다.
                             # 1행의 길이 = 4 vs 열(j)의 인덱스 0 1 2 3 따라서 j는 arr[i]행의 길이보다 작아야한다.
            print(arr[i][j], end="")