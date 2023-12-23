n = int(input())
arr = list(map(int, input().split()))
scores = [0] * 5
for i, score in enumerate(arr):
    scores[i] = score
    
def calculate(scores: list[int]):
    korea, math, english, science, foreign = scores
    ans = 0
    if korea > english:
        ans += abs(korea - english) * 508
    else:
        ans += abs(korea - english) * 108
        
    if math > science:
        ans += abs(math - science) * 212
    else:
        ans += abs(math - science) * 305
    
    ans += foreign * 707
    
    return ans * 4763

print(calculate(scores))