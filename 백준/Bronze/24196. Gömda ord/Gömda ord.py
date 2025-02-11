s = input()
ans = ''
idx = 0
while idx < len(s):
    ans += s[idx]
    idx += ord(s[idx]) - 64
print(ans)