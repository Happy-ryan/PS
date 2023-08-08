n = int(input())

bottles = list(range(1, n + 1))[::-1]
for i in bottles:
    if i == 1:
        print("1 bottle of beer on the wall, 1 bottle of beer.")
        print("Take one down and pass it around, no more bottles of beer on the wall.")
    elif i == 2:
        print(f"2 bottles of beer on the wall, 2 bottles of beer.")
        print(f"Take one down and pass it around, 1 bottle of beer on the wall.")  
    else:
        print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
        print(f"Take one down and pass it around, {i - 1} bottles of beer on the wall.")
    
    print()

print("No more bottles of beer on the wall, no more bottles of beer.")
if n == 1:
    print(f'Go to the store and buy some more, {n} bottle of beer on the wall.')
else:
    print(f'Go to the store and buy some more, {n} bottles of beer on the wall.')