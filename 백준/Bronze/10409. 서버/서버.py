n, T = map(int, input().split())
arr = list(map(int, input().split()))
sum = 0
sum_arr = []
for i in arr :
    sum += i
    if sum <= T :
        sum_arr.append(sum)

print(len(sum_arr))
