# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
# sabendo que a decisão
# é sempre pelo mais barato.
# Mostrar o resultado com duas casas decimais

'''

produto1 = float(input('Preço do arroz: '))
produto2 = float(input('Preço do feijão: '))
produto3 = float(input('Preço do ovo: '))
'''

p1 = float(input('Diga o valor do produto 1: '))
p2 = float(input('Diga o valor do produto 2: '))
p3 = float(input('Diga o valor do produto 3: '))

if p1 < p2 and p1 < p3:
    print(f'O {p1} é o produto mais barato')
elif p2 < p1 and p2 < p3:
    print(f'O {p2} é o produto mais barato')
elif p3 < p1 and p3 < p2:
    print(f'O {p3} é o produto mais barato')
else:
    print('Os produtos são equivalentes')







