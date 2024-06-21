# Exercicio 3.1 - pag 60 - 
def rigth_justify (s):
    
    tamanho = 70 - len(s) 
    string_formatad = s + "-" * tamanho
    print(string_formatad)
    


rigth_justify(input('Digite uma palavra: '))                   

