arr = []
for i in range(10) :
    x = int(input())
    arr.append(x)
result = [] 
for j in arr :
    plus = j % 42
    result.append(plus)
print(len(set(result)))