s1 = sorted(list(input()))
s2 = sorted(list(input()))
sum = 0
s1_set = set(s1)
s2_set = set(s2)
for x in s1_set:
    if x not in s2: #s1에만 있는 경우
        sum += s1.count(x)
    else: #s1 과 s2 모두 있는 경우
        sum += abs(s1.count(x)-s2.count(x))
for y in s2_set: # s2에만 있는 경우
    if y not in s1:
        sum += s2.count(y)

print(sum)