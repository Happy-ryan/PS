score = input()
A_val = 0
B_val = 0

for i in range(len(score)):
    if score[i] == "A":
        A_val += int(score[i + 1])
    elif score[i] == "B":
        B_val += int(score[i + 1])

if A_val > B_val:
    print("A")
else:
    print("B")