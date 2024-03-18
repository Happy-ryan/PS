score = input()
A_val = B_val = 0 

for i in range(0, len(score), 2):
    if score[i] == "A":
        A_val += int(score[i + 1])
    else:
        B_val += int(score[i + 1])

print("A" if A_val > B_val else "B")
