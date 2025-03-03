k = input()
cnt = k.count('0')
for i in range(len(k) - 1, -1, -1):
    if k[i] != '0':
        break
    cnt -= 1
print(cnt)