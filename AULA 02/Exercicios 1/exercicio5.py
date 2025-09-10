"""produto = 100
quantidade_produto=float(input("digite a quantidade desse produto: "))

if quantidade_produto > 10:
    print(produto * quantidade_produto)
"""

produto = float(input("Digite o valor desse produto: "))
quantidade_produto = int(input("Digite a quantidade desse produto: "))

if quantidade_produto > 10:
    produto = produto * 0.9

total = produto * quantidade_produto
print(f"Valor total: R${total:.2f}")