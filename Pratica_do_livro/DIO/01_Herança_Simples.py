### Em Python, a herança simples é o tipo mais básico dessa habilidade, onde uma classe filha herda de uma única classe pai. 
### É como ter um mentor experiente te guiando e te ensinando tudo o que sabe.


class Veiculo:
    def __init__(self, cor, placa, n_rodas):
        self.cor = cor;
        self.placa = placa;
        self.n_rodas = n_rodas;

    def ligar_motor(self):
        print('Motor Ligado!');

    def __str__(self):
        return self.cor


class Motocicleta(Veiculo):
    pass


class Carro(Veiculo):
    pass


class Caminhao(Veiculo):
    def __init__(self, cor, placa, n_rodas, carregado):
        super().__init__(cor, placa, n_rodas)
        self.carregado = carregado;

    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado!")


# moto = Motocicleta('Preta', 'ABD-234' , 2 );
# print(moto)
# moto.ligar_motor()

# carro = Carro('Branco', 'XDD-409', 4);
# carro.ligar_motor()

caminhao = Caminhao('Verde', 'sfd-342', 8, 'Sim');
caminhao.ligar_motor()
caminhao.esta_carregado()
print(caminhao)
