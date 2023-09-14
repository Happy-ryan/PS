row = ['+']
while True:
    s = input()
    if s == '=':
        break
    row.append(s)

cnt = 0
for i in range(0, len(row), 2):
    if row[i] == "+":
        cnt += int(row[i + 1])
    elif row[i] == "-":
        cnt -= int(row[i + 1])
    elif row[i] == "*":
        cnt *= int(row[i + 1])
    else:
        cnt //= int(row[i + 1])
        
print(cnt)