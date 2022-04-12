s = input().upper()
for i in s :
    if i not in "CAMBRIDGE" : # 캠브리지에 포함되지 않는다면(not in) 출력하도록
        print(i, end="")