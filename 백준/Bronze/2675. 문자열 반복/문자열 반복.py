T = int(input())
for _ in range(T) :
    arr = input()
    for j in range(2, len(arr)) :
        result = arr[j]*int(arr[0])
        print(result, end="")
    print('')