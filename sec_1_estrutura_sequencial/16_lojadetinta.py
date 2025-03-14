# Faça um programa para uma loja de tintas.
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de
# 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total

'''
print('Loja de tintas')
print('---------------')
print(' ')

cobertura = 3
lata_tinta = 18
preco_lata = 80

area = float(input('Qual o tamanho da área, em m²? '))

tamanho_cobertura = area / cobertura
lata_inteira = int(tamanho_cobertura / lata_tinta)

if (tamanho_cobertura%lata_tinta != 0):
    lata_inteira += 1

valor_total = lata_inteira * preco_lata

print(f'Tamanho da área: {area}m²')
print(f'Quantidade de tinta necessária: {tamanho_cobertura:.2f} litros')
print('Quantidade de latas necessárias: ', lata_inteira, ' latas')
print(f'Preço total: {valor_total:.2f} reais')
'''