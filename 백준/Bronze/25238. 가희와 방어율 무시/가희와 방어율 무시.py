a,b = map(int,input().split())
defence = a-(a*(b/100))
# print(defence)
if defence >= 100:
    print(0)
else: print(1)