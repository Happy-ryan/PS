s1 = input()
s2 = input() 
s3 = input()
arr = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
def resistanc(s) :
    for i in arr :
        if s == i :
            num = arr.index(i)
            return num

def mul(k) :
    for k in arr :
        if s3 == k :
            num = 10**(arr.index(k))
            return  num

num1 = resistanc(s1)
num2 = resistanc(s2)
num3 = mul(s3)

print((num1*num3*10)+(num2*num3))