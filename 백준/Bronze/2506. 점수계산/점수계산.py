n = int(input())
arr = list(input().split())
# print(arr)
sum = ""
score = 0
for x in arr:
    sum +=x
sum = sum.split('0')
# print(sum)
for row in sum:
    if '1' in row:
        for x in range(1,len(row)+1):
            score +=x

print(score)