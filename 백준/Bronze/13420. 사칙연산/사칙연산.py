def plus(a, b, c):
    if a + b == c:
        return 'correct'
    else: 
        return 'wrong answer'
        
def minus(a, b, c):
    if a - b == c:
        return 'correct'
    else:
        return 'wrong answer'
        
def mul(a, b, c):
    if a * b == c:
        return 'correct'
    else:
        return 'wrong answer'
    
def div(a, b, c):
    if a / b == c:
        return 'correct'
    else:
        return 'wrong answer'

t = int(input())
for _ in range(t):
    a, cmd, b, equal, c = input().split()
    a, b, c = int(a), int(b), int(c)
    if cmd == '+':
        print(plus(a, b, c))
    elif cmd == '-':
        print(minus(a, b, c))
    elif cmd == '*':
        print(mul(a, b, c))
    else:
        print(div(a, b, c))