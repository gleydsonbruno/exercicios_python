# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7
# Mostrar a área com 1 casa decimal.

altura = float(input('Qual sua altura?'))
peso_ideal_h = (72.7 * altura) - 58
peso_ideal_m = (62.1 * altura) - 44.7
print(f'Se você for homem, seu peso ideal é: {peso_ideal_h:.1f} kg')
print(f'Se você for mulher, seu peso ideal é: {peso_ideal_m:.1f} kg')

