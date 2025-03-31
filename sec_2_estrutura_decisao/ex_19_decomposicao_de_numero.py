"""
Exercício 19 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do
mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

    >> decompor_numero(1000)
    'O número precisa ser menor que 1000'
    >> decompor_numero(-1)
    'O número precisa ser positivo'
    >> decompor_numero(326)
    '326 = 3 centenas, 2 dezenas e 6 unidades'
    >> decompor_numero(300)
    '300 = 3 centenas'
    >> decompor_numero(100)
    '100 = 1 centena'
    >> decompor_numero(320)
    '320 = 3 centenas e 2 dezenas'
    >> decompor_numero(310)
    '310 = 3 centenas e 1 dezena'
    >> decompor_numero(305)
    '305 = 3 centenas e 5 unidades'
    >> decompor_numero(301)
    '301 = 3 centenas e 1 unidade'
    >> decompor_numero(311)
    '311 = 3 centenas, 1 dezena e 1 unidade'
    >> decompor_numero(111)
    '111 = 1 centena, 1 dezena e 1 unidade'
    >> decompor_numero(101)
    '101 = 1 centena e 1 unidade'
    >> decompor_numero(25)
    '25 = 2 dezenas e 5 unidades'
    >> decompor_numero(20)
    '20 = 2 dezenas'
    >> decompor_numero(21)
    '21 = 2 dezenas e 1 unidade'
    >> decompor_numero(10)
    '10 = 1 dezena'
    >> decompor_numero(16)
    '16 = 1 dezena e 6 unidades'
    >> decompor_numero(1)
    '1 = 1 unidade'
    >> decompor_numero(7)
    '7 = 7 unidades'

"""

def plural(y, word):
    if int(y) > 1:
        return word + 's'

    else:
        return word




def decompor(num: int):
    uni = 'unidade'
    dec = 'dezena'
    cen = 'centena'
    num = str(num)
    if len(num) == 1:
        print(num[0], plural(num, uni))
    elif len(num) == 2:
        if int(num[1]) < 1:
            print(num[0], plural(num[0], dec))
        else:
            print(num[0],plural(num[0], dec) ,num[1], plural(num[1], uni))
    else:
        if int(num[1]) < 1 and int(num[2]) < 1:
            print(num[0], plural(num[0], cen))
        elif int(num[1]) < 1:
            print(num[0], plural(num[0], cen), num[2], plural(num[2], uni))
        elif int(num[2]) < 1:
            print(num[0], plural(num[0], cen), num[1], plural(num[1], dec))
        else:
            print(num[0], plural(num[0], cen), num[1], plural(num[1], dec),  num[2], plural(num[2], uni))

num = int(input('Um número inteiro menor que 1000: '))

if num < 1:
    print('O número precisa ser positivo')
elif num >= 1000:
    print('O número precisa ser menor que 1000')
else:
    decompor(num)

