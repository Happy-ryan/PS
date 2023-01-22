from collections import Counter
s = int(input())
num = [ input()[::-1] for _ in range(s)]

i = 1
while True:
    student = Counter()
    for row in num:
        student[row[0 : i]] += 1
    if len(student.keys()) == s:
        print(i)
        break
    else:
        i += 1