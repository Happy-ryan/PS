cnt = 0
code = input()
n = int(input())
for _ in range(n):
    num = input()
    if code[:5] == num[:5]:
        cnt +=1
print(cnt)
