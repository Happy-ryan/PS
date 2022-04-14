T = int(input())
for _ in range(T) :
    cnt = 0
    N,M=map(int, input().split())
    for i in range(N, M+1) :
        arr = list(str(i)) # 0을 찾기 위해서 숫자를 문자열로 전환
        #print(arr)
        for j in range(len(arr)) : # 문자0의 개수를 찾기 위해서  for문 돌리기
            if arr[j] == "0" :
                cnt +=1
    print(cnt)