# https://www.acmicpc.net/problem/27541
n = int(input())
s =  list(input())

if s[-1] == "G":
    ans = s[:-1]
else:
    ans = ''.join(s) + "G"
    
print(''.join(ans))