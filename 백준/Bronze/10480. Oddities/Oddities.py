#10 is even
#9 is odd
#-5 is odd

t = int(input())
for _ in range(t):
    n = int(input())
    if n % 2 ==0: print(f"{n} is even")
    else: print(f"{n} is odd")