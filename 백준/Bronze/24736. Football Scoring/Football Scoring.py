score = [6,3,2,1,2]
arr = [ list(map(int,input().split())) for row in range(2)]

for row in arr:
    sum = 0
    for i in range(5):
        sum += (score[i]*row[i])
    print(sum,end=' ')