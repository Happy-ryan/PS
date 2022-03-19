arr=[]
for i in range(9) :
    x = int(input())
    arr.append(x)
max_num = max(arr)
line_num = arr.index(max(arr)) + 1
print(max_num)
print(line_num)