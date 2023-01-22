while True:
    t = int(input())
    if t == 0:
        break
    words = []
    for _ in range(t):
        word = input()
        words.append((word.upper(), word))
    
    words.sort(key = lambda x :x[0])

    print(words[0][1])