def eh_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numero = 29
if eh_primo(numero):
    print(f"{numero} é primo") 
else:
    print(f"{numero} não é primo")