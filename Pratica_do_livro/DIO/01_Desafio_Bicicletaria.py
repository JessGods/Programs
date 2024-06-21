class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print('PIMM PIMMMM')

    def parar(self):
        print('Bicicleta parada.')

    def correr(self):
        print('Vrummmmm...')

    @property
    def __str__(self):
        return f'{self.__class__.__name__}'
        {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}


b1 = Bicicleta('Verde', 'Calloi', 2024, 600)
b1.buzinar()
b1.correr()
b1.parar()
b1.buzinar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)
