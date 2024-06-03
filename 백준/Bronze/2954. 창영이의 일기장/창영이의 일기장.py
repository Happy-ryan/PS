s = input()
idx = len(s) - 1

answer = []
while idx > 0:
    if s[idx] ==  ' ':
        answer.append(' ')
        idx -= 1
    elif s[idx] in 'aeiou':
        answer.append(s[idx])
        idx -= 3
    elif s[idx] not in 'aeiou':
        answer.append(s[idx])
        idx -= 1
        
answer.append(s[0])

print(''.join(answer[::-1]))