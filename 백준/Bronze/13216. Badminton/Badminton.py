log = input()

A, B = 0, 0
score = [0, 0]

for c in log:
    if c == 'A':
        A += 1
    else:
        B += 1
    
    if A == 21 or B == 21:
        print(f"{A}-{B}")
        
        if A > B:
            score[0] += 1
        else:
            score[1] += 1
        
        A, B = 0, 0

print('A' if score[0] > score[1] else 'B')