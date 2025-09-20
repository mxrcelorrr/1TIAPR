import random

tentativas = 3
numero = random.randint(1, 10)

while  tentativas > 0:
    palpite = int(input("Digite um numero entre 1 e 10"))
    if palpite == numero:
        print("Parabens! vc acertou")
        break
    else:
        tentativas -= 1
        print(f"voce errou. tentativas restante: {tentativas}")
