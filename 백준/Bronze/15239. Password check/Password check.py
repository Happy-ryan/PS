t = int(input())

def solution(password):
    
    f1 = False 
    for x in 'abcdefghijklmnopqrstuvwxyz':
        if x in password:
            f1 = True
    
    f2 = False
    for x in 'abcdefghijklmnopqrstuvwxyz':
        if x.upper() in password:
            f2 = True
            
    f3 = False
    for x in password:
        if x.isdigit():
            f3 = True

    f4 = False
    for x in "}{+_)(*&^%$#@!./,;":
        if x in password:
            f4 = True
            
    f5 = False
    if len(password) >= 12:
        f5 = True
            
    if f1 and f2 and f3 and f4 and f5:
        return 'valid'

    return 'invalid'

for _ in range(t):
    n = int(input())
    password = input()
    print(solution(password))