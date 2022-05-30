arr = list(input())
sum = 0
for i in reversed(range(0,len(arr))):
    sum += int(arr[len(arr)-1-i])*(2**i)
result_ten = sum * 17
result_bin = bin(result_ten)
print(result_bin[2:])