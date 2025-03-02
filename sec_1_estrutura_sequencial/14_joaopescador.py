# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de
# seu trabalho.
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de
# São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
# João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
# Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa
# que João deverá pagar.
# Imprima os dados do programa com as mensagens adequadas.
# Mostrar o peso e multa com duas casas decimais

peso = float(input('Peso do peixe: '))
peso_excedido =  peso > 50
multa = 4
if peso_excedido:
    print(f'Seu peixe tem {peso:.2f} kg, passando {peso - 50:.2f} kg do peso estabelecido. Sua multa é de: {multa * (peso - 50):.2f}')
else:
    print(f'O peso do seu peixe é: {peso:.2f} kg, isento de multa.')