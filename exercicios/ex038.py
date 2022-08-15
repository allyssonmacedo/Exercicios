#Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com a sua idade se ele ainda vai se alistar ao serviço militar, se é hora de se alistar ou se já passou do tempo do alistamento.
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

import datetime

ano_nasc = int(input('Em que ano você nasceu? '))
idade = datetime.datetime.today().year - ano_nasc

if idade == 18:
    print('Você deverá se alistar ainda este ano')
elif idade < 18:
    anos_para_alistamento = 18 - idade
    print(f'Você ainda tem {anos_para_alistamento} anos para se alistar')
else: 
    idade > 18
    anos = idade - 18
    print(f'Você já deveria ter se alistado a {anos} anos atrás')
