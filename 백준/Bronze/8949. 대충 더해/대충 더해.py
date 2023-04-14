x, y = input().split()
la, ly = len(x), len(y)
if la > ly:
    y = '0'*(la-ly) + y
else:
    x = '0'*(ly-la) + x
res = ""
for i in range(len(x)):
    res += str(int(x[i]) + int(y[i]))
print(res)