def f(s):
    ans = ''
    for x in s[::-1]:
        if x == 'b':
            ans += 'd'
        elif x == 'd':
            ans += 'b'
        elif x == 'p':
            ans += 'q'
        elif x == 'q':
            ans += 'p'
        elif x == 'i' or x == 'o' or x == 'v' or x == 'w' or x == 'x':
            ans += x
        else:
            return 'INVALID'
    
    return ans

while True:
    s = input()
    if s == '#':
        break
    print(f(s))