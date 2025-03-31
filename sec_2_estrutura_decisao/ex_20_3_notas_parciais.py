"""
Exercício 20 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno
e presentar:
A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
A mensagem "Aprovado com Distinção", se a média for igual a 10.

    >> calcular_status(10, 4, 10)
    'Aprovado'
    >> calcular_status(0, 10, 0)
    'Reprovado'
    >> calcular_status(5, 8, 0)
    'Reprovado'
    >> calcular_status(10, 10, 10)
    'Aprovado com Distinção'
"""


def valida(media):
    if 7 <= media < 9.9:
        print('')
        print('Aprovado')
    elif media < 7:
        print('')
        print('Reprovado')
    elif media == 10:
        print('')
        print('Aprovado com distinção')


def calcular_status(notass: list):
    soma = 0
    for note in notass:
        soma += note

    media = soma / 3
    return valida(media)

notas = []
for nota in range(1, 4):
    notas.append(float(input(f'Digite sua {nota}º nota: ')))


calcular_status(notas)