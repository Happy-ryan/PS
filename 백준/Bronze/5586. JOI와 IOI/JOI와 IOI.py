num1, num2 = 0, 0
s = input()
for i in range(0, len(s)):
    if s[i: i + 3] == 'JOI':
        num1 += 1
    elif s[i : i + 3] == 'IOI':
        num2 += 1
print(num1)
print(num2)