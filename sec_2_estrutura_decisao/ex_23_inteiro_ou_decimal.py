"""
Exercício 23 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de
arredondamento.

    >> decidir_se_eh_inteiro_ou_decimal('256')
    'Inteiro'
    >> decidir_se_eh_inteiro_ou_decimal('1.0')
    'Inteiro'
    >> decidir_se_eh_inteiro_ou_decimal('2.0000')
    'Inteiro'
    >> decidir_se_eh_inteiro_ou_decimal('2.00001')
    'Decimal'
    >> decidir_se_eh_inteiro_ou_decimal('11.2')
    'Decimal'
    >> decidir_se_eh_inteiro_ou_decimal('3.1415')
    'Decimal'
"""


def decidir_se_eh_inteiro_ou_decimal(valor: float) -> str:
    valida = valor.is_integer() #utilizando a função da dica
    if not valida:
        print('NÚMERO DECIMAL')
    else:
        print('NÚMERO INTEIRO')

def decidir_se_eh_inteiro_ou_decimala(valor: float) -> str:

    if valor % 1 == 0: #utilizando apenas a razão
        print('NÚMERO INTEIRO')
    else:
        print('NÚMERO DECIMAL')

while True:
    decidir_se_eh_inteiro_ou_decimala(float(input('Um número que é: ')))
