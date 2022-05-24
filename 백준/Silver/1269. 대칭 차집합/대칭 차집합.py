A,B = map(int, input().split())
A_set = set(list(map(int, input().split())))
B_set = set(list(map(int, input().split())))
left = A_set - B_set
right = B_set - A_set
print(len(left)+len(right))