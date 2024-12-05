def pole(a, b, e):
    x = (b-a)/e
    pole = 0
    for i in range(e):
        y = (a+i*x) * (a+i*x) + 1
        pole += y*x
    return pole

print(pole(0, 4, 1000))

