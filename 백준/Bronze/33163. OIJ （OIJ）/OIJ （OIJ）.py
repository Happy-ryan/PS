n = int(input())
s = input()

ans = ''
for x in s:
    if x == 'J':
        ans += 'O'
    elif x == 'O':
        ans += 'I'
    else:
        ans += 'J'
        
print(ans)