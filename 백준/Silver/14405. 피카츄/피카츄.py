s = input()

idx = 0

flag = True
while idx < len(s):
    if s[idx:idx + 2] == 'pi':
        idx += 2
    elif s[idx:idx + 2] == 'ka':
        idx += 2
    elif s[idx:idx + 3] == 'chu':
        idx += 3
    else:
        flag = False
        break
    
print('YES' if flag else 'NO')