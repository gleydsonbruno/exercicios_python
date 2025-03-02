# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# usando a seguinte fórmula: (72.7*altura) - 58
# Mostrar a área com 1 casa decimal.

altura = float(input('Qual sua altura?'))
peso_ideal = (72.7 * altura) - 58
print(f'Seu peso ideal é: {peso_ideal:.1f} kg')
