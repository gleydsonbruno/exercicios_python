# Faça um Programa que leia três números e mostre o maior e o menor deles.

n1 = int(input('Digite um numero inteiro: '))
n2 = int(input('Digite mais um numero inteiro: '))
n3 = int(input('Digite mais um numero inteiro: '))
print('')
print(f' Números digitados: {n1}, {n2}, {n3}')
if n1 < n2 and n1 < n3:
    print(f'{n1} é o menor!')
elif n2 < n1 and n2 < n3:
    print(f'{n2} é o menor!')
elif n3 < n1 and n3 < n2:
    print(f'{n3} é o menor!')
else:
    print('Os números são equivalentes.')