n = int(input())

r, c = 0, 0

while True:
    if r * c >= n:
        break
    r += 1
    
    if r * c >= n:
        break
    c += 1
    
print(r, c)