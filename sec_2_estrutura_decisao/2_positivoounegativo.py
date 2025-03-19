# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
# Caso seja igual a 0, retorne None.

n1 = int(input('Um número: '))
if n1 < 0:
    print(f'{n1} é um número negativo')
elif n1 == 0:
    print('None')
else:
    print(f'{n1} é positivo')