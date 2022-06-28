arr = input()
sum1 = 0
sum2 = 0
for i in range(0,(len(arr)//2)):
    sum1 += int(arr[i])
for j in range((len(arr)//2),len(arr)):
    sum2 += int(arr[j])

if sum1 == sum2:
    print('LUCKY')
else : print('READY')