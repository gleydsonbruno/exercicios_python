# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
while True:
    letter = str(input('Digite apenas uma letra: ')).lower()
    blacklist = "!@#$%¨&*()_+{}[]1234567890 "
    l_blacklist = blacklist.split(',')




    if len(letter) > 1 or len(letter) < 1:
        print('Você deve digitar uma letra. Nada mais, nada menos.')
        print('')
    else:
        print('')
        if letter == "a" or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
            print('Essa letra é uma vogal.')
        elif letter in blacklist:
            print('Entrada inválida')
        else:
            print('Essa letra é consoante.')