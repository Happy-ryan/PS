L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
day1,day2 = 0,0
if A%C == 0:
    day1 += A//C
else: day1 += ((A//C)+1)
if B%D == 0:
    day2 += B//D
else : day2 += ((B//D)+1)
print(L-max(day1,day2))