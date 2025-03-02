# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
# Mostrar apenas valor inteiro da temperatura

cel = float(input('Quantos graus Celcius? '))
emfah = cel * 1.8 + 32 # // para mostrar o número inteiro (arredondando ou não)

print(f'{cel}ºC está fazendo {emfah}ºF convertido')