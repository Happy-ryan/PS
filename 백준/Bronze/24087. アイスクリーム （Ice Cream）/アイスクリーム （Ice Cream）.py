s = int(input())
a = int(input())
b = int(input())

val = 250

if s > a:
    val += ((s - a) // b) * 100
    if (s - a) % b != 0:
        val += 100
        
print(val)