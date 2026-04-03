s = input()

vowels = "aeiou"

for i in range(len(s) - 1, -1, -1):
    if s[i] in vowels:
        print(s[:i + 1] + "ntry")
        break