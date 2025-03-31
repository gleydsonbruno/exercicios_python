"""
Exercício 25 da seção de estrutura de decisão da Python Brasil:
https://wiki.python.org.br/EstruturaDeDecisao

Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

  "Telefonou para a vítima?"
  "Esteve no local do crime?"
  "Mora perto da vítima?"
  "Devia para a vítima?"
  "Já trabalhou com a vítima?"

O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeito",
entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente".

    >> investigar('Sim','Sim','Sim','Sim','Sim')
    'Assassino'
    >> investigar('Sim','Sim','Sim','Sim','Não')
    'Cúmplice'
    >> investigar('Sim','Sim','Sim','Não','Não')
    'Cúmplice'
    >> investigar('Sim','Sim','Não','Não','Não')
    'Suspeito'
    >> investigar('Sim','Não','Não','Não','Não')
    'Inocente'
    >> investigar('Não','Não','Não','Não','Não')
    'Inocente'

"""

def valida(ans):
    ans = ans.upper()
    if ans == 'sim'.upper():
        pass
    elif ans == 'não'.upper():
        pass
    else:
        print('Responda apenas com Sim ou Não', ans)


def investiga(sim):
    if sim < 2:
        print('INOCENTE')
    elif sim == 2:
        print('SUSPEITO')
    elif 2 < sim < 5:
        print('CÚMPLICE')
    elif sim == 5:
        print('ASSASSINO')
    else:
        print('what is wrong? ')

def investigar(tel: str, est: str, mora: str, dev: str, trab: str, ):
    respostas = [tel, est, mora, dev, trab]
    sim = 0
    nao = 0
    for resposta in respostas:
        resposta = resposta.upper()
        if resposta == 'SIM':
            sim += 1
        elif resposta == 'NÃO':
           nao += 1
        else:
            print('Respostas insuficientes')

    investiga(sim)



telefonou = input('Telefonou para a vítima?')
valida(telefonou)
local = input('Esteve no local do crime?')
valida(local)
mora_perto = input('Mora perto da vítima?')
valida(mora_perto)
devia = input('Devia para a vítima?')
valida(devia)
trabalhou = input('Já trabalhou com a vítima?')
valida(trabalhou)
print('')

investigar(telefonou, local, mora_perto, devia, trabalhou)
