from math import gcd

def solution(arr):
    LCM = arr[0]
    for i in range(1, len(arr)):
        LCM = (LCM * arr[i]) // gcd(LCM, arr[i]) 
        
    return LCM