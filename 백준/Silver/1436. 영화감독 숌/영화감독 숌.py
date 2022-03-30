n  = int(input())
arr = [666,6660,6661,6662,6663,6664,6665,6666,6667,6668,6669,1666,2666,3666,4666,5666,7666,8666,9666]

for i in range(0, 100) : # 66600
    ret1 = 66600
    ret1 += i 
    arr.append(ret1)
for i in range(1,10) : #06660
    for j in range(0,10) :
        ret2 = i*10000+6660
        ret2 += j
        arr.append(ret2)
for i in range(10,100) : #00666
    ret3 = 666
    ret3 += i*1000
    arr.append(ret3)
    
for i in range(0,1000) : #666000
    ret4 = 666000
    ret4 += i
    arr.append(ret4)

for i in range(1,10) : #066600
    for j in range(0,100) :
        ret5 = i*100000+66600
        ret5 += j
        arr.append(ret5)
for i in range(10, 100) : #006660
    for j in range(0, 10) :
        ret6 = i*10000+6660
        ret6+=j
        arr.append(ret6)
for i in range(100,1000) : #000666
    ret7 = 666
    ret7 += i*1000
    arr.append(ret7)

for i in range(0,10) : #6660000
    ret8 = 6660000
    ret8 += i
    arr.append(ret8)

for i in range(1,10) : #0666000
    for j in range(0,1000) :
        ret9 = i*1000000+666000
        ret9 += j
        arr.append(ret9)

for i in range(10,100) : #0066600
    for j in range(0,100) :
        ret10 = i*100000+66600
        ret10 += j
        arr.append(ret10)

for i in range(100, 1000) : #0006660
    for j in range(0,10) :
        ret11 = i*10000 + 6660
        ret11 += j
        arr.append(ret11)

for i in range(1000,10000) : #0000666
    ret12=666
    ret12 += i*1000
    arr.append(ret12)

s_set = set(arr)
s_sort = sorted(s_set)
print(s_sort[n-1])