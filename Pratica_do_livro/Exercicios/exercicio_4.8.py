def main (num1 = '2', num2 = '1'):
    #n1 = float(input('Digite o primeiro número: ')); #'Digite o primeiro número: '
    n1 = float(num1); #'Digite o primeiro número: '
    #n2 = float(input('Digite o segundo número: ')); #'Digite o segundo número: '
    n2 = float(num2); #'Digite o segundo número: '
    operacao = input('Qual operação você deseja?  Adição[+]  Subtração[-]  Divisão[/]  Multiplicação[*] ');
    
    if operacao == '+':
        print(n1+n2);
    elif operacao == '-':
        print(n1-n2);
    elif operacao == '/':
        print(n1/n2);
    elif operacao == '*':
        print(n1*n2);
    else:
        print('Erro')
    



main(4,3);
               