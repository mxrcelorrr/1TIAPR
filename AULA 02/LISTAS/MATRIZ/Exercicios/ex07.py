matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

a , b , c = matriz[0]
d , e , f = matriz[1]
g , h , i = matriz[2]

det = a * (e * i - f * h) - b * (d * i - f *g) + c * (d * h - g * e)
print(f"o determinante da matriz eh: {det}")