""""
Um programa para controlar as entregas de mercadorias, para que as entregas fossem mais rápidas

Ele deve receber variáveis de entrada:
    Data, Motorista, Endereço, Quantidade de caixas, Loja

    data = data

    motorista = motorista

    endereco = endereco

    quant_Cxs = Quantidade de caixas

    loja = loja

"""

import json
from datetime import datetime
from datetime import date

def main():

    
    
    def pergunta_loja():
            while True:
                 try:
                    loja = int(input('Qual a loja referente?\n(1)Loja 1  (2)Loja 2  (3)Loja 3  (4)Loja 4  (5)Loja 5 \n\n --> '))
                    if 1 <= loja <= 5:
                        
                        if loja == 1:
                            print('Loja 1 Selecionada! Rua Paraná, 201 - Riachuelo Batatais/SP\n\n')
                            break
                        elif loja == 2:
                            print('Loja 2 selecionada! Av. Dr. Amador de Barros, 1265 - Castelo Batatais/SP\n\n')
                            break
                        elif loja == 3:
                            print('Loja 3 selecionada! Av. Dr. Amador de Barros, 1265 - Castelo Batatais/SP\n\n')
                            break
                        elif loja == 4:
                            print('Loja 4 selecionada! Av. Ayrton Senna, 800 - Aeroporto Batatais/SP\n\n')
                            break
                        elif loja == 5:
                            print('Loja 5 selecionada! Avenida Coronel Antonio Justino de Figueiredo, 545 - Cecap Altinópolis-SP\n\n')
                            break
                    else: 
                         print('Opção não encontrada, favor selecione uma Loja válida.\n\n')
                 except ValueError:
                      print('O valor digitado não é um numero, tente novamente! ')
                     
                      
    pergunta_loja()
    
    def pegar_addres():
            rua = input('Qual a Rua? ')
            n_casa = int(input('Qual o número da casa? '))
            bairro = input('Qual o bairro? ')
            quant_Cxs = int(input('Qual a quantidade de caixas? '))

            endereco = (f'\n\n\nRua: {rua}, N°:{n_casa}, Bairro: {bairro}, N°caixas: {quant_Cxs}')
            return endereco
    
    ### Coleta de dados 
   
    data_hora = datetime.now()
    data_h_format = data_hora.strftime("%d/%m/%y")

    motorista = input('Nome do Motorista: ')
    ENTRADA = f'\n\n\nHoje é Dia: {data_h_format}.\nTenha um bom dia de trabalho {motorista}!'
    endereco = pegar_addres()
    #lista_endereco = [endereco]

    print(endereco)
    print(ENTRADA)
    
    
    #loja = int(input('Qual a loja referente?\n(1)Loja 1  (2)Loja 2  (3)Loja 3  (4)Loja 4  (5)Loja 5 \n '))
   
    

main()

