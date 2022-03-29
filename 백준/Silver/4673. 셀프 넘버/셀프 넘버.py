num1 = range(1,10)
num2 = range(10, 10000)
arr = []
for i in num1 :
   result = i*2
   arr.append(result)
for j in num2 :
    result = j
    for k in range(len(str(j))) :
        result += int(str(j)[k])
    arr.append(result)
for n in range(1, 10000):
    if n not in arr :
        print(n)