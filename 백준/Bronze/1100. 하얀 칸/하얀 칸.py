cnt = 0
s0 = input()
s1 = input()
s2 = input()
s3 = input()
s4 = input()
s5 = input()
s6 = input()
s7 = input()

for i in [s0[0],s0[2],s0[4],s0[6]] :
    if i == "F" :
        cnt +=1
for i in [s2[0],s2[2],s2[4],s2[6]] :
    if i == "F" :
        cnt +=1
for i in [s4[0],s4[2],s4[4],s4[6]] :
    if i == "F" :
        cnt +=1
for i in [s6[0],s6[2],s6[4],s6[6]] :
    if i == "F" :
        cnt +=1
for i in [s1[1],s1[3],s1[5],s1[7]] :
    if i == "F" :
        cnt +=1
for i in [s3[1],s3[3],s3[5],s3[7]] :
    if i == "F" :
        cnt +=1
for i in [s5[1],s5[3],s5[5],s5[7]] :
    if i == "F" :
        cnt +=1
for i in [s7[1],s7[3],s7[5],s7[7]] :
    if i == "F" :
        cnt +=1
print(cnt)