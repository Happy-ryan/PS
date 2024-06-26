n = int(input())
s1 = input()
s2 = input()

cnt = 0
for x1, x2 in zip(s1, s2):
    if x1 != x2:
        cnt += 1
        
print(cnt)