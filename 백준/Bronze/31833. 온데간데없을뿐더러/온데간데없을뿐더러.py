n = int(input())

X = int(''.join(list(input().split())))
Y = int(''.join(list(input().split())))

print(X if X <= Y else Y)