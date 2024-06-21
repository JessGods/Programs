def aumento_salario():
    salario = float(input('Qual o valor do salário?  '))
    total = 0
    aumento = 0 

    if salario >= 1250:
        aumento = salario * 0.1
        total = aumento + salario
        print(f'Seu salário foi aumentado em R${aumento:.2f}, total do salario: R${total:.2f}')
    
    elif salario < 1250:
        aumento = salario * 0.15
        total = aumento + salario
        print(f'Seu salário foi aumentado em R${aumento:.2f}, total do salario: R${total:.2f}')


aumento_salario()