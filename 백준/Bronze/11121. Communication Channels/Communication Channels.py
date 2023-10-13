# your code goes here
t = int(input())

def f(a, b):
    for i in range(len(a)):
        if a[i] != b[i]:
            return "ERROR"
    return "OK"

for _ in range(t):
    a, b = input().split()
    print(f(a, b))