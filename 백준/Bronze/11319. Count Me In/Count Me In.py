t = int(input())
for _ in range(t):
    s = input().lower()
    c, v = 0, 0
    
    for x in s:
        if x == ' ':
            continue
        if x in 'aeiou':
            v += 1
        else:
            c += 1
            
    print(c, v)