s = input()
A, B = 0, 0
for x in s:
    if x == 'A':
        A += 1

B = len(s) - A

print(f'{A} : {B}')