# Faça um Programa que peça dois números e imprima o maior deles.

n1 = float(input('Um número: '))
n2 = float(input('Outro número: '))

if n1 > n2:
    print(f'{n1} é maior que {n2}')
elif n1 == n2:
    print('Os valores são iguais')
else:
    print(f'{n2} é maior que {n1}')