from collections import Counter
from itertools import combinations

def mul(tup):
    mul = 1
    for x in tup:
        mul *= (x + 1)
    return mul
        
        
def solution(clothes):
    answer = 0
    cloth_dict = dict()
    for name, cloth in clothes:
        if cloth not in cloth_dict.keys():
            cloth_dict[cloth] = 1
        else:
            cloth_dict[cloth] += 1
            
    choice = cloth_dict.values()
    answer = mul(choice) - 1        
    return answer