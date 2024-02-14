s = input()
cnt1 = 0
cnt2 = 0
for x in s:
    if x in 'aeiou':
        cnt1 += 1
    if x in 'aeiouy':
        cnt2 += 1
        
print(cnt1, cnt2)