a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))
d = b**2 - 4 * a * c
if d >= 0:
    x1 = (-1 * b + d**0.5) / (2 * a)
    x2 = (-1 * b - d ** 0.5) / (2 * a)
    if d == 0:
        print(f'Answer: {x1}')
    else:
        print(f'Answer: {x1}; {x2}')
else:
    print('No answer')
