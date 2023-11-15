n = int(input())
s = input()
sum_val = 0
for x in s:
    sum_val += ord(x) - 64
    
print(sum_val)