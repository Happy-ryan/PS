N = int(input())
if N == 1 :
    None
else :
    for i in range(2, N+1) :
        while N % i == 0 :
            N = N/i
            print(i)
            if N%i != 0 :
                break