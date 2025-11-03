n = int(input())
Y = input()
T = input()

res = 0

for i in range(n):
    if Y[i] =='C' and T[i] == 'C':
        res += 1

print(res)