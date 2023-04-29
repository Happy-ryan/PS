# https://www.acmicpc.net/problem/8371
n = int(input())
s1 = input()
s2 = input()
sum_val = 0
for i in range(n):
    if s1[i] != s2[i]:
        sum_val += 1
        
print(sum_val)