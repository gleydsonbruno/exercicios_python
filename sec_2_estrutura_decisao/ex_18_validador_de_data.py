"""
Exercício 18 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

    >> validar_data('')
    'Data inválida'
    >> validar_data('1')
    'Data inválida'
    >> validar_data('1/2/2004')
    'Data válida'
    >> validar_data('1/02/2004')
    'Data válida'
    >> validar_data('01/02/2004')
    'Data válida'
    >> validar_data('30/02/2004')
    'Data inválida'
    >> validar_data('01/13/2004')
    'Data inválida'

"""

#solução adotada pelo github


def validar_data(data: str):
    dia = int(data[0:2])
    mes = int(data[3:5])
    ano = int(data[6:10])

    bissexto = False
    if ano % 4 == 0:
        bissexto = True
        if (ano % 100 == 0) and (ano % 400 != 0):
            bissexto = False

    valida = True
    if mes in (1, 2, 3, 5, 7, 8, 10, 12):
        if (dia < 1) or (dia > 31):
            valida = False

    elif mes in (4, 6, 9, 11):
        if dia < 1 or dia > 30:
            valida = False
    elif mes not in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12):
        valida = False
    else:
        if bissexto:
            if (dia < 1) or (dia > 29):
                valida = False
            else:
                if (dia < 1) or (dia > 28):
                    valida = False

    if valida:
        print('Data válida')
    else:
        print('Data inválida')





    print(f'Data: {dia}/{mes}/{ano}')

data = str(input('Escreva uma data válida (dd/mm/yyyy): '))
validar_data(data)