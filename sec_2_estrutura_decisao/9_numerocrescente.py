# Faça um Programa que leia três números e mostre-os em ordem decrescente.


n1 = int(input('Digite número: '))
n2 = int(input('Digite número: '))
n3 = int(input('Digite número: '))


if n1 < n2:
    n1, n2 = n2, n1
if n1 < n3:
    n1, n3 = n3, n1
if n2 < n3:
    n2, n3 = n3, n2

print(f'Ordem decrescente dos números: {n1}, {n2}, {n3}')
