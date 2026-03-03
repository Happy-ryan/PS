t = int(input())

for _ in range(t):
    
    N, X, Y = map(int, input().split())
    colors = list(map(int, input().split()))
    
    easy_wrong = (colors[0] == X)
    hard_wrong = (colors[-1] == Y)
    
    if easy_wrong and hard_wrong:
        print("BOTH")
    elif easy_wrong:
        print("EASY")
    elif hard_wrong:
        print("HARD")
    else:
        print("OKAY")