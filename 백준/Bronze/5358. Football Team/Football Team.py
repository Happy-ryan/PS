
while True:
    try:
        s = input()
        ans = ''
        for i in range(len(s)) :
            if s[i] == 'e' : 
                ans += 'i'
            elif s[i] == 'i' : 
                ans += 'e'
            elif s[i] == 'E' : 
                ans += 'I'
            elif s[i] == 'I' : 
                ans += 'E'
            else :
                ans += s[i]
        print(ans)    
    except:
        break