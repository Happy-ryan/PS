def isPrime(x):
    flag = True
    for i in range(2, int(x**(1/2)) + 1):
        if x % i == 0:
            flag = False
    return flag

# 65- A, Z - 90 // 97 - a, 122- b
from collections import defaultdict

arr = 'abcdefghijklmnopqrstuvwxyz'
dic = defaultdict()
for x in arr:
    dic[x] = ord(x) - 96
    dic[x.upper()] = ord(x.upper()) - 38
res = 0
s = input()
for x in s:
    res += dic[x]

if isPrime(res):
    print('It is a prime word.')
else:
    print('It is not a prime word.')