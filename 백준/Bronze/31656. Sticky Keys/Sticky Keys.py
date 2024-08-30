s = input()

stack = []

for x in s:
    if not stack:
        stack.append(x)
    else:
        if stack[-1] != x:
            stack.append(x)
            
            
print(''.join(stack))