side = [4, 100, 67, 5, 6, 8, 9, 12, 456, 98, 34]
square = 0
side.sort(reverse=True)
while square == 0:
    a = side[0]
    b = side[1]
    c = side[2]
    if a + b > c and a + c > b and b + c > a:
        p = (a + b + c) / 2
        square = (p*(p - a)*(p - b)*(p - c))**0.5
    else:
        side.pop(0)
print(square)
print(a, b, c)
