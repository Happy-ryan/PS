k1, o1, k2, o2, k3 = input().split()

def cal1(k1, o1, k2, o2, k3):
    
    k1, k2, k3 = int(k1), int(k2), int(k3)
    
    sum_val = 0
    if o1 == '+':
        sum_val += k1 + k2
    elif o1 == '-':
        sum_val += k1 - k2
    elif o1 == '*':
        sum_val += k1 * k2
    else:
        if k2 < 0:
            k2 *= -1
            sum_val += k1 // k2 
            sum_val *= -1
        elif k1 < 0:
            k1 *= -1
            sum_val += k1 // k2
            sum_val *= -1
        else:
            sum_val += k1 // k2
            
    if o2 == '+':
        sum_val += k3
    elif o2 == '-':
        sum_val -= k3
    elif o2 == '*':
        sum_val *= k3
    else:
        if k3 < 0:
            k3 *= -1
            sum_val //= k3
            sum_val *= -1
        elif sum_val < 0:
            sum_val *= -1
            sum_val //= k3
            sum_val *= -1
        else:
            sum_val //= k3
        
    return sum_val

def cal2(k1, o1, k2, o2, k3):
    
    k1, k2, k3 = int(k1), int(k2), int(k3)
    
    sum_val = 0
    if o2 == '+':
        sum_val += k2 + k3
    elif o2 == '-':
        sum_val += k2 - k3
    elif o2 == '*':
        sum_val += k2 * k3
    else:
        if k3 < 0:
            k3 *= -1
            sum_val += k2 // k3
            sum_val *= -1
        elif k2 < 0:
            k2 *= -1
            sum_val += k2 // k3
            sum_val *= -1
        else:
            sum_val += k2 // k3
            
    if o1 == '+':
        k1 += sum_val
    elif o1 == '-':
        k1 -= sum_val
    elif o1 == '*':
        k1 *= sum_val
    else:
        if sum_val < 0:
            sum_val *= -1
            k1 //= sum_val
            k1 *= -1
        elif k1 < 0:
            k1 *= -1
            k1 //= sum_val
            k1 *= -1
        else:
            k1 //= sum_val
        
    return k1

res1 = cal1(k1, o1, k2, o2, k3)
res2 = cal2(k1, o1, k2, o2, k3)

print(min(res1, res2))
print(max(res1, res2))