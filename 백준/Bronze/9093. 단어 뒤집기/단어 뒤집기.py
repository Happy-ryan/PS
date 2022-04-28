N = int(input())
arr = [ input().split() for _ in range(N)] # 문자열 이차원배열하기
for i in range(N) :
    for j in range(len(arr[i])) : 
        print(arr[i][j][::-1],end=" ") # 한 줄로 출력 end
    print() # 다음 문자열을 다음 줄에 출력해야하므로 앞에 뒤에 포문이 끝나고 앞의 포문에 들어가기 전에
            # 엔터시키기 = print()