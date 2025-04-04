"""
Exercício 21 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar
quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo
é de 1 real e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma
nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10,
uma nota de 5 e quatro notas de 1.

    >> calcular_troco(256)
    '2 notas de R$ 100, 1 nota de R$ 50, 1 nota de R$ 5 e 1 nota de R$ 1'
    >> calcular_troco(1)
    '1 nota de R$ 1'
    >> calcular_troco(5)
    '1 nota de R$ 5'
    >> calcular_troco(10)
    '1 nota de R$ 10'
    >> calcular_troco(11)
    '1 nota de R$ 10 e 1 nota de R$ 1'
    >> calcular_troco(399)
    '3 notas de R$ 100, 1 nota de R$ 50, 4 notas de R$ 10, 1 nota de R$ 5 e 4 notas de R$ 1'
"""



'''
def calcular_troco(valor: int) -> str:
    qtd = len(str(valor))
    if valor < 5:
        print(f'{valor} notas de $ 1')
    elif valor == 5:
        print(f'1 nota de R$ {valor}')
    elif 5 < valor < 10:
        print(f'1 nota de 5, {valor - 5} notas de R$ 1')
    elif valor == 10:
        print(f'1 nota de R$ 10')
    elif 10 < valor < 50:
        

def valida_saque(value: int):
    if value < 1:
        print('O valor mínimo para saque é de 1 real')
    elif value > 600:
        print('O valor máximo para saque é de 600 reais')
    else:
        calcular_troco(value)


saque = int(input('Valor do saque:'))
valida_saque(saque)
'''




