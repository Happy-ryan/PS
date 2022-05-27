N = int(input())
cnt = 0
while N != 0:
    for i in range(1,N+1):
        N -= i
        if N >= 0:
            cnt += 1
        else:
            N += i
            break # 처음부터 다시 for문을 돌아야한다. 숫자가 부족한 경우 1부터 다시 시작한다는 단서// 따라서 break로 for문 탈출
print(cnt)
