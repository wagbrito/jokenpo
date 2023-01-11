import os
import random

#placar
placar_jogador = 0
placar_computador = 0

#opções
itens = ('Papel', 'Pedra', 'Tesoura')

while True:
    print('='*47)
    print('Bem vindo(a) ao jogo do Pedra, Papel ou Tesoura')
    print('='*47)
    print()
    print('Placar')
    print('Você: {}'.format(placar_jogador))
    print('Computador: {}'.format(placar_computador))
    print()
    print('0 - Papel | 1 - Pedra | 2 - Tesoura')
    
    jogador = int(input('Qual a sua jogada? '))
    computador = random.randint(0,2)
    
    print('Sua jogada: {}'.format(itens[jogador]))
    print('Jogada do computador: {}'.format(itens[computador]))

    if jogador == 0: #se o jogador jogar Papel
        if computador == 0: #se o computador jogar Papel
            print('Empate')
        elif computador == 1: #se o computador jogar Pedra
            print('O jogador vence')
            placar_jogador = placar_jogador + 1
        elif computador == 2: #se o computador jogar Tesoura
            print('O computador vence')
            placar_computador = placar_computador + 1
    
    if jogador == 1: #se o jogador jogar Pedra
        if computador == 1: #se o computador jogar Pedra
            print('Empate')
        elif computador == 2: #se o computador jogar Tesoura
            print('O jogador vence')
            placar_jogador = placar_jogador + 1
        elif computador == 0: #se o computador jogar Papel
            print('O computador vence')
            placar_computador = placar_computador + 1
              
    if jogador == 2: #se o jogador jogar Tesoura
        if computador == 2: #se o computador jogar Tesoura
            print('Empate')
        elif computador == 0: #se o computador jogar Papel
            print('O jogador vence')
            placar_jogador = placar_jogador + 1
        elif computador == 1: #se o computador jogar Pedra
            print('O computador vence')
            placar_computador = placar_computador + 1

    print('')
    print('='*30)
    print('Jogar novamente? 0 - SIM | 1 - NÃO')
    if int(input()) == 1:
        break