t = int(input())
for i in range(1,t + 1):
    user_input = list(input().split("="))
    left = user_input[0].strip()
    right = user_input[1].strip()
    if eval(left) != int(right):
        print(f"Case {i}: NO")
    else:
        print(f"Case {i}: YES")