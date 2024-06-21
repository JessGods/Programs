velocidade = int(input('Qual a velocidade do carro? '))
if velocidade > 80:
    valor_multa = (velocidade - 80) * 5 ;

    print('Você foi multado no valor de: R$',valor_multa)
else:
    print(velocidade,'KMh')