# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido
# Mostrar os resultados com duas casas decimais

valor_hora = float(input('Quanto você ganha por hora de trabalho? '))
horas_trabalhadas = float(input('Quantas horas você trabalha por semana? '))
horas_mensais = horas_trabalhadas * 4

salario = valor_hora * horas_mensais
total_descontos = (salario * 0.08) + (salario * 0.11) + (salario * 0.05)



print(f'Seu salário bruto é de: R$ {salario}')
print(f'Descontos:')
print('')
print(f'INSS: R$ {salario * 0.08:.2f}')
print(f'IRPF: R$ {salario * 0.11:.2f}')
print(f'SINDICATO: R$ {salario * 0.05:.2f}')
print(f'Desconto total: R$ {total_descontos:.2f}')
print('')
print(f'Seu salário líquido é de: R$ {salario - total_descontos:.2f}')