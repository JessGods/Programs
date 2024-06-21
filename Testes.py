

product1 = 'Computer';
product2 = 'Office desk';

age = int(30);
code = 5290;
gender = 'F';

price1 = float(2100.0) ;
price2 = float(650.5) ;

measure = float(53.2345674) ;

def imprime_p(n,s) :
    print(f'{n}, witch price is ${s}')

def imprime_m(p):
    print(f'Measue witch eight decimal places: {p:.9}')
    print(f'Rouded (three decimal places): {p:.5}')
    print(f'Us decimal points: {p:.5g}')

print('Products: ')
imprime_p(product1, price1)
imprime_p(product2, price2)
print(f'\nRecord: {age} years old, code {code} and gender: {gender}\n')
imprime_m(measure)