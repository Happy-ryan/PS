# 문제 포인트 : 각 col(열)기준으로 가장 많이 나온 것을 선택해야 최소가 될 수 있음.
n,m = map(int,input().split())
arr = [input() for row in range(n)]
# print(arr)
# print(arr[0])
# print(arr[0][1])
dna = ''
cnt = 0
for j in range(m): #col
    dna_dict={'A':0,'C':0,'G':0,'T':0}
    for i in range(n): #row
        if arr[i][j] =="A":
            dna_dict['A'] += 1 #value에 더할 수 있더라...
        elif arr[i][j] =="C":
            dna_dict['C'] += 1
        elif arr[i][j] =="G":
            dna_dict['G']  += 1
        else : dna_dict['T'] +=1
    dna_value_list = list(dna_dict.values())#list(dict.values()) = value로 구성된 리스트 생성
    dna_tuple_list = list(dna_dict.items()) #list(dict.items()) = (key,value)튜플로 구성된 리스트 생성
    max_value = max(dna_value_list)
    max_value_idx = dna_value_list.index(max_value) #가장 많이 나온 알파벳을 출력하기 위해서 인덱스 찾는 과정

    dna += (dna_tuple_list[max_value_idx])[0] #많이 나온 알파벳의 숫자가 같으면 사전순이기 때문에 <9 line>부터 사전순으로 미리 배치했다.
    cnt += max_value
print(dna)
print(n*m-cnt)