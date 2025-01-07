n = int(input())
s = input()
ans = ''
for idx in range(0, len(s), n):
    ans += s[idx]
print(ans)