# https://www.acmicpc.net/problem/11091
def f(s: str):
    check = [0] *26
    for x in s:
        if 'a' <= x <= 'z' or 'A' <= x <= 'Z':
            x = x.upper() 
            x = ord(x) - 65
            if check[x] == 0:
                check[x] = 1
    return check
    
t = int(input())
for _ in range(t):
    s = input()
    if sum(f(s)) == 26:
        print('pangram')
    else:
        ans = 'missing '
        post = []
        for idx, x in enumerate(f(s)):
            if x == 0:
                post.append(chr(idx + 65).lower())
        post.sort()
        ans = ans + ''.join(post)
        print(ans)