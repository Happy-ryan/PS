arr = input().split()
# 리스트 안의 문자열에서 U,C,P,C대문자를 더하는 함수
def f(list):
    arr =[]
    for row in list:
        for x in row:
            if x in "UCPC":
                arr.append(x)
    return arr
# 리스트 안의 문자열 더하는 함수
def str_sum(list):
    str = ''
    for x in list:
        str += x
    return str

result = list(enumerate(f(arr)))
ucpc=[]
ucpc_idx_U = [0]
ucpc_idx_C = [0]
ucpc_idx_P =[0]
ucpc_idx= [0]

for tup in result:
    if tup[1]=="U":
        ucpc.append(tup[1])
        ucpc_idx_U.append(tup[0])
        break
for tup in result[ucpc_idx_U[-1]+1:]:
    if tup[1] =="C":
        ucpc.append(tup[1])
        ucpc_idx_C.append(tup[0])
        break
for tup in result[ucpc_idx_C[-1]+1:]:
    if tup[1] =="P":
        ucpc.append(tup[1])
        ucpc_idx_P.append(tup[0])
        break

for tup in result[ucpc_idx_P[-1]+1:]:
    if tup[1] =="C":
        ucpc.append(tup[1])
        ucpc_idx_C.append(tup[0])
        break

if str_sum(ucpc) =="UCPC":
    print("I love UCPC")
else: print("I hate UCPC")
# print("ucpc_idx_U",ucpc_idx_U)
# print("ucpc_idx_C",ucpc_idx_C)
# print("ucpc_idx_P",ucpc_idx_P)