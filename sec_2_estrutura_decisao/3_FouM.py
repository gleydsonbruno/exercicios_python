# Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Retorne: F - Feminino ou M - Masculino. Para quaisquer outros valores, retorne Sexo Inválido.

print('Responda apenas com F ou M.')
a = True
while a:
    genero = str(input('Você é F ou M? ')).upper()
    if genero == "F":
        print('F - Feminino')
        a = False
    elif genero == "M":
        print('M - Masculino')
        a = False
    else:
        print('Sexo inválido!')
