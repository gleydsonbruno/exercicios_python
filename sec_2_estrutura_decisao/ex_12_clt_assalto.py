"""
Exercício 12 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que
depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do
Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos
os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
  Salário Bruto até 900 (inclusive) - isento
  Salário Bruto até 1500 (inclusive) - desconto de 5%
  Salário Bruto até 2500 (inclusive) - desconto de 10%
  Salário Bruto acima de 2500 - desconto de 20%

Mostrar valores monetários com duas casas decimais, alinhados à direita, com espaço para 5 dígitos de salário, ou seja,
até R$ 99999,99

    >> calcular_salario_liquido(1, 160)
    Salário Bruto: (R$ 1.00 * 160)     : R$   160.00
    (-) IR (0%)                        : R$     0.00
    (-) INSS (10%)                     : R$    16.00
    (-) Sindicato (3%)                 : R$     4.80
    FGTS (11%)                         : R$    17.60
    Total de descontos                 : R$    20.80
    Salário Liquido                    : R$   139.20
    >> calcular_salario_liquido(5, 220)
    Salário Bruto: (R$ 5.00 * 220)     : R$  1100.00
    (-) IR (5%)                        : R$    55.00
    (-) INSS (10%)                     : R$   110.00
    (-) Sindicato (3%)                 : R$    33.00
    FGTS (11%)                         : R$   121.00
    Total de descontos                 : R$   198.00
    Salário Liquido                    : R$   902.00
    >> calcular_salario_liquido(10, 160)
    Salário Bruto: (R$ 10.00 * 160)    : R$  1600.00
    (-) IR (10%)                       : R$   160.00
    (-) INSS (10%)                     : R$   160.00
    (-) Sindicato (3%)                 : R$    48.00
    FGTS (11%)                         : R$   176.00
    Total de descontos                 : R$   368.00
    Salário Liquido                    : R$  1232.00
    Salário Bruto: (R$ 100.00 * 160)   : R$ 16000.00
    (-) IR (20%)                       : R$  3200.00
    (-) INSS (10%)                     : R$  1600.00
    (-) Sindicato (3%)                 : R$   480.00
    FGTS (11%)                         : R$  1760.00
    Total de descontos                 : R$  5280.00
    Salário Liquido                    : R$ 10720.00

"""

sind = 0.03
fgts = 0.11
inss = 0.1

valor_hora = float(input('Qual o valor da sua hora de trabalho? '))
qtd_horas_trabalhadas = float(input('Qual a quantidade de horas trabalhadas no mês? '))
salario_bruto = qtd_horas_trabalhadas * valor_hora
if salario_bruto <= 900:
    ir = 0.0
    total_descontos = (sind * salario_bruto) + (inss * salario_bruto) + (ir * salario_bruto)

    print(f'Salário bruto: (R$ {valor_hora:5.2f} * {qtd_horas_trabalhadas}) : R$ {salario_bruto:8.2f}')
    print(f'(-) IR (0%)                  : R$ {ir * salario_bruto:8.2f}')
    print(f'(-) INSS (R$ 10%)             : R$ {(inss * salario_bruto):8.2f}')
    print(f'(-) Sindicato (3%)            : R$ {(sind * salario_bruto):8.2f}')
    print(f'FGTS (11%)                    : R$ {fgts * salario_bruto:8.2f}')
    print(f'Total de descontos            : R$ {total_descontos:8.2f}')
    print(f'Salário líquido               : R$ {(salario_bruto - total_descontos):8.2f}')
elif 900 < salario_bruto <= 1500:
    ir = 0.05
    total_descontos = (sind * salario_bruto) + (inss * salario_bruto) + (ir * salario_bruto)

    print(f'Salário bruto: (R$ {valor_hora:5.2f} * {qtd_horas_trabalhadas}) : R$ {salario_bruto:8.2f}')
    print(f'(-) IR (5%)                   : R$ {ir * salario_bruto:8.2f}')
    print(f'(-) INSS (R$ 10%)             : R$ {(inss * salario_bruto):8.2f}')
    print(f'(-) Sindicato (3%)            : R$ {(sind * salario_bruto):8.2f}')
    print(f'FGTS (11%)                    : R$ {fgts * salario_bruto:8.2f}')
    print(f'Total de descontos            : R$ {total_descontos:8.2f}')
    print(f'Salário líquido               : R$ {(salario_bruto - total_descontos):8.2f}')
elif 1500 < salario_bruto <= 2500:
    ir = 0.1
    total_descontos = (sind * salario_bruto) + (inss * salario_bruto) + (ir * salario_bruto)

    print(f'Salário bruto: (R$ {valor_hora:5.2f} * {qtd_horas_trabalhadas}) : R$ {salario_bruto:8.2f}')
    print(f'(-) IR (10%)                  : R$ {ir * salario_bruto:8.2f}')
    print(f'(-) INSS (R$ 10%)             : R$ {(inss * salario_bruto):8.2f}')
    print(f'(-) Sindicato (3%)            : R$ {(sind * salario_bruto):8.2f}')
    print(f'FGTS (11%)                    : R$ {fgts * salario_bruto:8.2f}')
    print(f'Total de descontos            : R$ {total_descontos:8.2f}')
    print(f'Salário líquido               : R$ {(salario_bruto - total_descontos):8.2f}')

