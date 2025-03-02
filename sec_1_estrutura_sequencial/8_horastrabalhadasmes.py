# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.
# Mostrar salário com duas casas decimais

salario = float(input('Quanto você ganha por hora? '))
horas = float(input('Quantas horas você trabalha semanalmente? '))
print(f'Você recebe, aproximadamente: R$ {salario * (horas*4)}')