N,M = map(int,input().split())
cnt = 0
while True:
    if N ==0 or M == 0 or N ==1 or M==1:
        break
    else:
        N -=2
        M -=2
        cnt +=1
print(cnt)