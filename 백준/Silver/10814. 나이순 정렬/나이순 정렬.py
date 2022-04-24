N = int(input())
arr=[input().split() for _ in range(N)]
result_list = [ [] for _ in range(210)]
for i in range(N) :
    result_list[int(arr[i][0])].append(arr[i])
for x in result_list :
    if x == [] :
        pass
    else :
        for row in x:
            print(*row)