arr = [input() for _ in range(9)]

tiger = arr.count('Tiger')
lion = arr.count('Lion')

print('Tiger' if lion < tiger else 'Lion')
