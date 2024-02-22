s = input()
bomb = input()

stack = []
idx = 0
while idx < len(s):
    if len(stack) < len(bomb):
        stack.append(s[idx])
    else:
        if ''.join(stack[-len(bomb):]) == bomb:
            for _ in range(len(bomb)):
                stack.pop()
        stack.append(s[idx])
    idx += 1
    
if ''.join(stack[-len(bomb):]) == bomb:
    for _ in range(len(bomb)):
        stack.pop()
        
if len(stack) == 0:
    print("FRULA")
else:
    print(''.join(stack))
