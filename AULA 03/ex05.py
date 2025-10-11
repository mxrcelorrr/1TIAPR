def fatorial(x = 6):
    y = x
    for i in range(2,y):
        x *= i
    return x
print(fatorial())
