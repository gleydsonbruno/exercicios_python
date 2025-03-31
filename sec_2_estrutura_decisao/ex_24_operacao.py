"""
Exercício 24 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da
operação deve ser acompanhado de uma frase que diga se o número é:
  par ou ímpar;
  positivo ou negativo;
  inteiro ou decimal.

Mostre o restultado com duas casas decimais

    >> fazer_operacao_e_classificar(2, 3, '+')
    Resultado: 5.00
    Número é impar, positivo e inteiro.
    >> fazer_operacao_e_classificar(-4, 2, '/')
    Resultado: -2.00
    Número é par, negativo e inteiro.
    >> fazer_operacao_e_classificar(0, 2, '*')
    Resultado: 0.00
    Número é par, neutro e inteiro.
    >> fazer_operacao_e_classificar(-3.14, 2, '*')
    Resultado: -6.28
    Número é negativo e decimal.
    >> fazer_operacao_e_classificar(3.14, 2, '-')
    Resultado: 1.14
    Número é positivo e decimal.

"""

def validacoes(n):
    parImpar(n)
    posNeg(n)
    isDecimal(n)

def parImpar(n):

    if n % 2 == 0:
        print('PAR')
    elif n % 2 == 1:
        print('IMPAR')
    else:
        pass

def posNeg(n):
    if n < 0:
        print('NÚMERO NEGATIVO')
    elif n == 0:
        print('NÚMERO NEUTRO')
    else:
        print('NÚMERO POSITIVO')

def isDecimal(n):
    if n % 1 == 0:
        print('NÚMERO INTEIRO')
    else:
        print('NÚMERO DECIMAL')

def fazer_operacao_e_classificar(n1: float, n2: float, operador: str):
    if operador == '+':
        resultado = n1 + n2
        print(f'{n1} {operador} {n2} é igual a {resultado:.2f}')
        validacoes(resultado)
    elif operador == '-':
        resultado = n1 - n2
        print(f'{n1} {operador} {n2} é igual a {resultado:.2f}')
        validacoes(resultado)
    elif operador == '*':
        resultado = n1 * n2
        print(f'{n1} {operador} {n2} é igual a {resultado:.2f}')
        validacoes(resultado)
    elif operador == '/':
        resultado = n1 / n2
        print(f'{n1} {operador} {n2} é igual a {resultado:.2f}')
        validacoes(resultado)
    else:
        print('operador inválido')

n1 = float(input('Digite um numero: '))
n2 = float(input('Digite outro numero: '))
operador = input('Digite a operação que deseja realizar (responda apenas com +, - , / ou *)')
print('')

fazer_operacao_e_classificar(n1, n2, operador)
