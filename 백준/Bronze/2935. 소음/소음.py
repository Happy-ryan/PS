def cal(a, cmd, b):
    if cmd == '+':
        return a + b
    else:
        return a * b
    
a = int(input())
cmd = input()
b = int(input())

print(cal(a, cmd, b))