arr = list(map(int, input().split()))
day = 1
cnt = 0
while True:
    day += arr[1]
    if day <= arr[0]:
        cnt +=1
    else : break     
print(cnt*arr[2]*arr[3])                              