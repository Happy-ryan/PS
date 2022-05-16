N = int(input())
for _ in range(N):
    s = input()
    stack=[]
    ans="YES" # 미리 답변 설정해놓기 #13번라인과 같이 ans만 바꾸기 위해서 미리 두는 것. 안그럼 print를 두 깨 써야해서 안좋다.
    for x in s:
        if x=="(":
            stack.append("(")
        else: 
            if "(" in stack:
                stack.pop()
            else: 
                ans = "NO" # 이곳에 print를 두면 출력이 두 번 되어버린다.
    if len(stack) != 0:
        ans = "NO"
    print(ans)
        