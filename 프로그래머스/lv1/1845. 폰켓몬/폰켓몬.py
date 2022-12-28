from collections import Counter
def solution(nums):
    answer = 0
    choice = len(nums)//2
    monsters = Counter(nums)
    answer = min(choice, len(monsters.keys()))
    return answer