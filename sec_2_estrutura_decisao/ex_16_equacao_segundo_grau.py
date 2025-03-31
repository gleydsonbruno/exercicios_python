"""
Exercício 16 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os
 valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
a) Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os
 demais valores, sendo encerrado;
b) Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
c) Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
d) Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário.

Mostrar raízes com uma casa decimal.

    >> resolver_equacao_do_segundo_grau(0, 3, 4)
    'Valor do coeficiente a deve ser diferente de 0'
    >> resolver_equacao_do_segundo_grau(2, 1, 2)
    'Delta negativo (-15), por isso não existem raízes reais'
    >> resolver_equacao_do_segundo_grau(1, 2, 1)
    'Delta é 0, raíz única no valor de -1.0'
    >> resolver_equacao_do_segundo_grau(1, 4, 3)
    'Delta é 4, raízes são -1.0 e -3.0'

"""

def valor_delta(delta, x1, x2):
    print(f'Delta: {delta:.2f}, Raíz 1: {x1:.2f}, Raíz 2: {x2:.2f}')

def resolver_equacao_do_segundo_grau(a: float, b: float, c: float):

    delta = b ** 2 - 4 * a * c
    x1 = (-b - delta ** 0.5) / (2 * a) # primeira raiz
    x2 = (-b + delta ** 0.5) / (2 * a) # segunda raiz

    if a == 0:
        print('Não há como ser função de 2º grau com valor de A sendo 0.')

    if delta < 0:
        print('A equação não possui raízes reais.')
        valor_delta(delta, x1, x2)
    elif delta == 0:
        print('A equação possui apenas uma raíz real.')
        valor_delta(delta, x1, x2)
    if delta > 0:
        print('A equação possui duas raizes reais.')
        valor_delta(delta, x1, x2)

a = float(input('Valor de a: '))
b = float(input('Valor de b: '))
c = float(input('Valor de c: '))

resolver_equacao_do_segundo_grau(a, b, c)