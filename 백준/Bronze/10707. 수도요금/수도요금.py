A = int(input())
B = int(input())
C = int(input())
D = int(input())
P = int(input())
x_cost = A*P
if P>C:
    y_cost = B + (P-C)*D
else: y_cost = B
print(min(x_cost,y_cost))