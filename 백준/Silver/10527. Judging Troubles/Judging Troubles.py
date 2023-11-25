from collections import Counter

n = int(input())
A = Counter([input() for _ in range(n)])
B = Counter([input() for _ in range(n)])

sum_val = 0
for key in A.keys():
    sum_val += min(A[key], B[key])
    
print(sum_val)