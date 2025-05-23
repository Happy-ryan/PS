h1, b1 = map(int, input().split())
h2, b2 = map(int, input().split())

p1 = b1 + (h1 * 3) 
p2 = b2 + (h2 * 3) 

if p2 < p1:
    print(f'{1} {p1 - p2}')
elif p1 < p2:
    print(f'{2} {p2 - p1}')
else:
    print('NO SCORE')