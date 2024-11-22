s = input()
sum_val = 0
for _ in range(len(s)):
    s = s[-1] + s[:-1]
    sum_val += int(s)
    
print(sum_val)