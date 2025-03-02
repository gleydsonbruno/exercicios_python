# Faça um programa que calcule a média de 4 notas

nota_temp = 0
for nota in range(4):
    nota_temp += float(input(f'Qual sua {nota+1}º nota?: '))

print(f'Sua média, baseado nas suas notas, foi de: {nota_temp / 4}')