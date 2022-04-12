N = int(input())
arr=list(map(int, input().split()))
cnt = 0
seat = [0]*101
for i in arr :
    seat[i] += 1
for j in range(1,101) :
    if seat[j] >= 2 :
        cnt += (seat[j]-1)
print(cnt)