s = input()
arr = 'aeiou'
cnt = 0
for x in s:
    if x in arr:
        cnt +=1
print(cnt)