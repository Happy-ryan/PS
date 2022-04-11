s = input() # 문자열 입력
s_list = list(s) # 문자열 리스트로 분해
arr=[0] # 첫 번째는 무조건 포함이기 때문에 선언시에 0은 미리 포함
for i in range(1, len(s_list)) :
    if ord(s[i]) == 45 : # 하이픈 뒤의 문자의 인덱스를 알기 위해서
        arr.append(i+1) # arr는 0을 제외하고는 하이픈 뒤 문자의 인덱스를 의미
result = "" # 문자열(정답)초기화
for j in arr :
    result += s_list[j] #s_list에 하이픈 뒤의 문자 찾기 : arr에 인덱스 전부 존재
print(result)