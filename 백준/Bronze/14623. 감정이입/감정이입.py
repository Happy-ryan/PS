num1 = input()
num2 = input()
# int(xx, 2): 2진수 xx를 10진수로 변경
ans = bin(int(num1, 2) * int(num2, 2))[2:]
print(ans)