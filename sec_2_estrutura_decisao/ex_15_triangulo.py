"""
Exercício 15 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo.
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;

    >> classificar_triangulo(2, 3, 4)
    'Triângulo Escaleno'
    >> classificar_triangulo(2, 2, 3)
    'Triângulo Isósceles'
    >> classificar_triangulo(2, 2, 2)
    'Triângulo Equilátero'
    >> classificar_triangulo(2, 2, 5)
    'Não é um triângulo'
    >> classificar_triangulo(5, 2, 2)
    'Não é um triângulo'
    >> classificar_triangulo(2, 5, 2)
    'Não é um triângulo'

"""


def classificar_triangulo(a, b, c):
    if a + b < c or a + c < b or b + c < a:
        print('Não é um triângulo!')
    elif a == b and b == c and a == c:
        print('Triângulo Equilátero')
    elif a != b and a != c and b != c:
        print('Triângulo Escaleno')
    elif a == b and b != c or b == c and c != a:
        print('Triângulo Isósceles')
    else:
        print('Tem parada errada aí')

a = int(input('Vamos formar um triângulo. Me diga o valor de um dos lados: '))
b = int(input('Me informe outro valor: '))
c = int(input('Só mais um valor: '))

classificar_triangulo(a, b, c)