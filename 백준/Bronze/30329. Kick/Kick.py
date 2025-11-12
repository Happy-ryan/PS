s = input()

cnt = 0
for i in range(len(s) - 3):
    x = s[i:i + 4]
    if x == 'kick':
        cnt += 1
        
print(cnt)