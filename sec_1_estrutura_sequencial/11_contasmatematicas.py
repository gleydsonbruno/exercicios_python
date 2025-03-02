# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#  1) o produto do dobro do primeiro com metade do segundo;
#  2) a soma do triplo do primeiro com o terceiro;
#  3) o terceiro elevado ao cubo.

n1 = int(input('Um número inteiro: '))
n2 = int(input('Outro número inteiro: '))
n3 = float(input('Agora um número real: '))

first = 2 * ( n1 * 2) + (n2 / 2)
second = (n1 * 3) + n3
third = n3 * n3 * n3

print(f' Enunciado 1: {first }, E2: {second}, E3: {third:.2f}')