# A97, B98, C99, D100... X 120, Y121, Z122
s = input()
ans = ''
for x in s:
    if x == 'A' or x == 'B' or x == 'C':
        ans += chr(ord(x) + 23)
    else:
        ans += chr(ord(x) - 3)

print(ans)