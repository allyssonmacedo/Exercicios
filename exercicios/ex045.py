#Crie um programa que faça o computador jogar Jokenpô com você.
import time
import random

while True:
    print(""" 
    1 - Pedra
    2 - Papel 
    3 - Tesoura """)
    escolha = int(input('Digite o número correspondente: '))
    
    if escolha == 1:
        item = 'Pedra'
    elif escolha == 2:
        item = 'Papel'
    elif escolha == 3:
        item = 'Tesoura'

    time.sleep(1)
    print('O computador está escolhendo...')
    time.sleep(3)
    computador = random.randint(1,3)


    if computador == 1:
        item_comp = 'Pedra'
    elif computador == 2:
        item_comp = 'Papel'
    elif computador == 3:
        item_comp = 'Tesoura'
    else:
        print('....')

    if escolha == computador:
        print(f'Empate!. Vocês escolheram {item}')
    elif (escolha == 1 and computador == 3) or (escolha == 2 and computador == 1) or (escolha == 3 and computador == 2) :
        print(f'[Computador escolheu {item_comp}]Parabéns, você ganhou.')
    else:
        print(f'[Computador escolheu {item_comp}] Você perdeu, o computador ganhou.')

    novo = str(input('Deseja jogar novamente? S/N '))
    if novo == 'S' or novo == 's':
        pass
    else:
        break
