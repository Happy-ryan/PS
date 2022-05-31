floor = [[0 for _ in range(15)] for _ in range(15)]
# 0층 채우기, j은 열이다.
for j in range(1,15):
    floor[0][j] = j
for i in range(1, 15): # i번째 층일 때 j번 포문돌려서 합 찾으면 주민
    sum = 0  
    for j in range(1,15): 
        sum += floor[i-1][j] # 호수가 늘어날 때마다 인원의 누적 합을 의미한다.
        floor[i][j] = sum
T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    print(floor[k][n])