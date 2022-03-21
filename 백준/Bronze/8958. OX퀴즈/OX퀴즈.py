n = int(input())
for _ in range(n) :
    arr = input()
    sum1 = 0
    sum2 = 0
    for j in range(len(arr)) :
        if arr[j] == "O" :
            sum1 += 1
            sum2 += sum1
        elif arr[j] == "X" :
            sum1 = 0
    print(sum2)