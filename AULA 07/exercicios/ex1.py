class veiculos:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    def info(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}"

carro = veiculos("McLaren", "Senna", 2025)
print(carro.info())

    

