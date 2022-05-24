sum = 0
for _ in range(4):
    s = int(input())
    sum +=s
min = sum//60
print(min)
print(sum - 60*min)