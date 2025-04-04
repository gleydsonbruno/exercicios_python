"""
Exercício 14 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e
calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for
A, B ou C ou “REPROVADO” se o conceito for D ou E.05

Mostar valores com uma casa decimal.

    >> calcular_conceito(10, 9)
    Notas: 10.0 e 9.0.
    Média: 9.5
    Conceito: A
    Status: APROVADO
    >> calcular_conceito(8.5, 7.5)
    Notas: 8.5 e 7.5.
    Média: 8.0
    Conceito: B
    Status: APROVADO
    >> calcular_conceito(7, 6)
    Notas: 7.0 e 6.0.
    Média: 6.5
    Conceito: C
    Status: APROVADO
    >> calcular_conceito(6.2, 4)
    Notas: 6.2 e 4.0.
    Média: 5.1
    Conceito: D
    Status: REPROVADO
    >> calcular_conceito(2.2, 1.2)
    Notas: 2.2 e 1.2.
    Média: 1.7
    Conceito: E
    Status: REPROVADO

"""


def calcular_conceito(nota_1, nota_2):
    media = (nota_1 + nota_2) / 2
    situacao = ''
    print(f'Sua 1º nota: {nota_1}')
    print(f'Sua 2º nota: {nota_2}')
    print(f'Média: {media}')
    if 9 <= media <= 10:
        print('Conceito A')
        situacao = 'APROVADO'
    elif 7.5 <= media < 9:
        print('Conceito: B')
        situacao = 'APROVADO'
    elif 6 <= media < 7.5:
        print('Conceito: C')
        situacao = 'APROVADO'
    elif 4 <= media < 6:
        print('Conceito: D')
        situacao = 'REPROVADO'
    elif 0 <= media < 4:
        print('Conceito: E')
        situacao = 'REPROVADO'
    print(f'Situação: {situacao}')


a = float(input('Sua primeira nota em história: '))
b = float(input('Sua segunda nota em história: '))
calcular_conceito(a, b)