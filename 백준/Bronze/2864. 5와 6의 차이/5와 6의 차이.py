def max_cal(s):
    s = list(s)
    for i, x in enumerate(s):
        if x == '5':
            s[i] = '6'
    
    return ''.join(s)

def min_cal(s):
    s = list(s)
    for i, x in enumerate(s):
        if x == '6':
            s[i] = '5'
    
    return ''.join(s)

a, b = input().split()
c = a
d = b

if '5' in a:
    Max_a = max_cal(a)
else:
    Max_a = a
if '5' in b:
    Max_b = max_cal(b)
else:
    Max_b = b

max_k = int(Max_a) + int(Max_b)

if '6' in c:
    Min_c = min_cal(c)
else:
    Min_c = c
if '6' in d:
    Min_d = min_cal(d)
else:
    Min_d = d

min_k = int(Min_c) + int(Min_d)

print(min_k, max_k)