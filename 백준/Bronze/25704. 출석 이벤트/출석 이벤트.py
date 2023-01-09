N = int(input())
P = int(input())
sale = [0]

if N >= 5 :
    sale.append(500)	
if N >= 10 :
    sale.append(P * 0.1)
if N >= 15 :
    sale.append(2000)	
if N >= 20 :
    sale.append(P * 0.25)	

res = P - max(sale)
if res < 0 :	
    res = 0	
    print(res)
else:
    print(f"{res:.0f}")