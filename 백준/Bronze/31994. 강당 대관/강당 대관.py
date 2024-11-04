arr = [list(input().split()) for _ in range(7)]
arr.sort(key= lambda x: -int(x[1]))
print(arr[0][0])