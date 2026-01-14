n = int(input())

vowels = set("aeiou")

for _ in range(n):
    word = input().strip()
    cnt = 0
    
    for ch in word:
        if ch in vowels:
            cnt += 1
    
    print(f"The number of vowels in {word} is {cnt}.")
