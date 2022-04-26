# 이 문제의 포인트는 나보다 키와 몸무게가 모두 큰 사람이 몇 명인지 세고 
# 그 숫자에 +1만 하게 되면 나의 등수가 된다.
N = int(input())
arr = [ list(map(int, input().split())) for _ in range(N)]
for i in range(N) :
    cnt = 1
    for j in range(N) :
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1] : # < 써버리면 ==가 아니기 때문에 나는 포함안되고 전부를 비교할 수 있다.
            cnt += 1
    print(cnt, end=" ")