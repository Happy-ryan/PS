N, M = map(int,input().split())
arr= list(map(int, input().split()))
max_list = []
for i in range(N) :                       #전체 경우의 수를 파악하기 위해서 인덱스를 통해서 수형도 그려보자
    for j in range(i+1, N) :              # i = 0 j= 1 k = 2 or 3 or 4 중복이 발생하기 때문에
        for k in range(j+1, N) :          # 삼중포문으로 전체경우의 수 파악하기
            if arr[i]+arr[j]+arr[k] > M :
                continue
            else :
                max_list.append(arr[i]+arr[j]+arr[k])

print(max(max_list))