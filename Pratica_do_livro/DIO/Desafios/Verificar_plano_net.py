# TODO: Crie uma Função: recomendar_plano para receber o consumo médio mensal:
def recomendar_plano(consumo_medio):
    consumo_medio = consumo_medio
    
    if consumo_medio <= 10:
      recomendar_plano = ('Plano Essencial Fibra - 50Mbps');
      
    elif consumo_medio < 20:
      recomendar_plano = ('Plano Prata Fibra - 100Mbps');
    
    else:
      recomendar_plano = ('Plano Premium Fibra - 300Mbps');
    
    
    return recomendar_plano
    
# TODO: Crie uma Estrutura Condicional para verifica o consumo médio mensal 
# TODO: Retorne o plano de internet adequado:
    

# Solicita ao usuário que insira o consumo médio mensal de dados:
consumo = float(input())
# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
print(recomendar_plano(consumo))