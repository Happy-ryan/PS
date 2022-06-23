n = int(input())
arr = [input() for _ in range(n)]
std = list(arr[0])
# print(std)
# std[1] = '?'
# print(std)
for i  in range(1,n):
    row = list(arr[i])
    for j in range(len(row)):
        if std[j] == row[j]:
            pass
        else:
            std[j] ='?'
for x in std:
    print(x,end='')