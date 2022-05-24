import math
D,H,W = map(int, input().split())
k = H*H+W*W
result = math.sqrt((D*D)/k)
H_arr =[]
W_arr=[]
for x in range(1,1000):
    if H*result >= x:
        H_arr.append(x)
for y in range(2,1010):
    if W*result >= y:
        W_arr.append(y)
print(H_arr[-1],W_arr[-1])