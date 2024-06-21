# Programa 4.3 - Cálculo do imposto de renda
salario = float(input('Digite o salário para o Cálculo: '))
base = salario
imposto = 0

if base > 3000:
    imposto = imposto + ((base - 3000)* 0.35)
    base = 3000
elif base > 1000:
    imposto = imposto + ((base - 1000)*0.20)

print(f'Salario: R${salario:6.2f}, O imposto a pagar é de: R${imposto:6.2f}')