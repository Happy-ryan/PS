S = input()+' ' # 마지막 종료되는 곳에 공백이나 닫는 가로가 없으면 cur을 추가 안해서 공백 넣어줌
cur = ''
ans = ''
switch = 0 # 1 '<' 로 열려 있는 상태 // 0 '>'  닫여 있는 상태
# < > 안의 공백과 단어 사이의 공백을 구분해야 
for s in S:
    if s == ' ' and switch == 0: # <>안의 공백 아님 & 공백만나면 ans에 넣고 cur 다시 초기화
        ans += cur[::-1]
        ans += s
        cur = ''
    elif s == '<':
        ans += cur[::-1] # 여는 가로 만나면 공백만나는 것과 유사하게 이때까지 단어들 뒤집고 cur 초기화
        cur =''
        switch = 1 
        cur += s # '여는 가로' 
    elif s == '>': # 닫는 가로 만나면 '< xx ..'가 cur에 저장되어있으니까 저장하고 종료 / 
        ans += cur
        ans += s # '닫는 가로'
        cur = ''
        switch = 0
    else:
        cur += s
list_ans = list(ans)
list_ans.pop()
final = ''
for x in list_ans:
    final += x
print(final)
