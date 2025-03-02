# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9)
# Mostrar apenas valor inteiro da temperatura

fah = float(input('Quantos graus Fahrenheit? '))
emcelsius = 5 * ((fah - 32) // 9) # // para mostrar o número inteiro (arredondando ou não)

print(f'{fah}ºF está fazendo {emcelsius}ºC convertido')