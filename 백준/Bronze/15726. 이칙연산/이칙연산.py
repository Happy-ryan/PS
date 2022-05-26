import math
A,B,C = map(int, input().split())
print(math.trunc(max((A*B/C),(A/B)*C)))