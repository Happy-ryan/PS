n = int(input())
words = list(input().split())

s = ''
for w in words:
    s += w
    s += 'DORO'
    s += ' '
    
print(s)