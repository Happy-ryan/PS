n = int(input())
s = input()

def f(s):
    cnt = 0 
    for x in s:
        if x == 'o':
            cnt += 1
        else:
            cnt = 0
            
        if cnt >= 3:
            return 'Yes'
        
    return 'No'
    
    
print(f(s))