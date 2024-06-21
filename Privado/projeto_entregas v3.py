""""
Um programa para controlar as entregas de mercadorias, para que as entregas fossem mais rápidas

Ele deve receber variáveis de entrada:
    Data, Motorista, Endereço, Quantidade de caixas, Loja

    data = data

    motorista = motorista

    endereco = endereco

    quant_Cxs = Quantidade de caixas

    loja = loja

    ultima att: 18/05
"""
import os
import json
from datetime import datetime

def main():

    
    
    def pergunta_loja():
            while True:
                 try:
                    loja = int(input('Qual a loja referente?\n(1)Loja 1  (2)Loja 2  (3)Loja 3  (4)Loja 4  (5)Loja 5 \n --> '))
                    if 1 <= loja <= 5:
                        
                        if loja == 1:
                            print('Loja 1 Selecionada! Rua Paraná, 201 - Riachuelo Batatais/SP\n')
                            break
                        elif loja == 2:
                            print('Loja 2 selecionada! Av. Dr. Amador de Barros, 1265 - Castelo Batatais/SP\n')
                            break
                        elif loja == 3:
                            print('Loja 3 selecionada! Av. Dr. Amador de Barros, 1265 - Castelo Batatais/SP\n')
                            break
                        elif loja == 4:
                            print('Loja 4 selecionada! Av. Ayrton Senna, 800 - Aeroporto Batatais/SP\n')
                            break
                        elif loja == 5:
                            print('Loja 5 selecionada! Avenida Coronel Antonio Justino de Figueiredo, 545 - Cecap Altinópolis-SP\n')
                            break
                    else: 
                         print('Opção não encontrada, favor selecione uma Loja válida.\n\n')
                 except ValueError:
                      print('O valor digitado não é um numero, tente novamente! ')
                     
                      
    pergunta_loja()
    
    def pegar_addres():
        enderecos_validos = []
        while True:
            endereco = input('\nDigite o endereço da entrega (Ou deixe vazio para finalizar):  ')
            if not endereco:
                os.system('cls')
                break
                

            if endereco:  
                enderecos_validos.append(endereco)  # Adiciona endereço na lista
                
                print(f'Endereço "{endereco}" adicionado com sucesso!')
            else:
                print('Endereço inválido ou incompleto. Por favor digite novamente.')

        return enderecos_validos  # Return the list of valid addresses

           
 
    def save_address(endereços, fileaddress): #Salva o endereço em um arquivo json
        with open(fileaddress, 'w') as f:
            json.dump(endereços, f)

    def load_address(fileaddress):
        try:
            with open(fileaddress, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []


    ### Coleta de dados 
    data_hora = datetime.now()
    data_h_format = data_hora.strftime("%d/%m/%y")

    motorista = input('Nome do Motorista: ')
    ENTRADA = f'\n\n\nHoje é Dia: {data_h_format}.\nTenha um bom dia de trabalho {motorista}!'
    
    #armazena end:
    enderecos_digitados = pegar_addres()

    #conta range da lista:
    i = range(len(enderecos_digitados))
    
    #Salva:
    save_address(enderecos_digitados,'enderecos.json')

    #carrega end:
    enderecos_carregados = load_address('enderecos.json')

    #mostra end:
    frase_final = 'Endereços para entregar:\n'
    tamanho_frase = len(frase_final)
    print(tamanho_frase*'_')
    print(frase_final)

    for indices in i:
        print(indices, save_address(indices) )
    #for endereco in enderecos_digitados:
    #     print(endereco)

    
    #lista_endereco = [endereco]

    print(ENTRADA)
    
main()

