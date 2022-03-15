H, M= map(int, input().split())
if 24>H>0 and M >= 45 :
    print(H, M-45)
elif 24>H>0 and 45 > M >=0 :
    print(H-1, 60-(45-M)) 
elif H==0 and M >= 45 :
    print(H, M-45 ) 
elif H==0 and 45>M>=0 :
    print(23, 60-(45-M) )