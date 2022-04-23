N, K = map(int, input().split())
M = N*K
arr = [list(map(int, input().split())) for _ in range(N)] #리스트컴프리헨션으로 N행 만들기
# 행렬의 빈칸 만들기 > 나중에 채우기
brr = [[0 for _ in range(M)] for _ in range(M)] # 첫번째 for문 행 * 두번째 for문 열
#print(brr) 
for i in range(N) :
    for j in range(N) :
        for i2 in range(i*K,(i+1)*(K)) : # i = 0,1 > K배 확대 > i=0 : 0, 1 (2) // i=1 : 2, 3 (4) range로 생각하면 가로의 2, 4 range(x, 2x)형태로 범위 설정가능
            for j2 in range(j*K,(j+1)*K):
                brr[i2][j2] = arr[i][j]
for s in brr :
    print(*s)