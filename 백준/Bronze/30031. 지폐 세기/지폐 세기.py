def f(w):
    if w == 136:
        return 1000
    if w == 142:
        return 5000
    if w == 148:
        return 10000
    return 50000

t = int(input())
sum_val = 0
for _ in range(t):
    w, h = map(int, input().split())
    sum_val += f(w)
    
print(sum_val)