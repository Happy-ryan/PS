import sys
a, b, v = map(int, sys.stdin.readline().split())
p = v-a
q = a-b
#n = ((v-a)/(a-b))
if p%q == 0 :
    day = p//q +1
    print(day)
else :
    day = p//q +2
    print(day)