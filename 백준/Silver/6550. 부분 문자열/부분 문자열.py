def f(s, t):
    idx_t = 0
    idx_s = 0
    ans = ''
    while idx_t < len(t) and idx_s < len(s):
        if t[idx_t] == s[idx_s]:
            ans += t[idx_t]
            idx_s += 1
        idx_t += 1
    
    if s == ans:
        return 'Yes'
    
    return 'No'

while True:
    try:
        s, t = input().split()
        print(f(s, t))
    except:
        break
    