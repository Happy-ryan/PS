T = int(input())
sum = ""
for _ in range(T) :
    arr = input()
    sum=""
    for j in range(2, len(arr)) :
        result = arr[j]*int(arr[0])
        sum = sum + result
    print(sum)
        