import os
import random

#placar
placar_jogador = 0
placar_computador = 0

#opções
itens = ('Papel', 'Pedra', 'Tesoura')

while True:
    os.system('cls')
    print('='*47)
    print('Bem vindo(a) ao jogo do Pedra, Papel ou Tesoura')
    print('='*47)
    print()
    print('PLACAR')
    print('Você: {}'.format(placar_jogador))
    print('Computador: {}'.format(placar_computador))
    print()
    print('0 - Papel | 1 - Pedra | 2 - Tesoura')
    print()
    jogador = int(input('Qual a sua jogada? '))
    computador = random.randint(0,2)
    print()
    print('Sua jogada: {}'.format(itens[jogador]))
    print('Jogada do computador: {}'.format(itens[computador]))
    print()

    if jogador == computador: #se o jogador e computador fizerem a mesma escolha
        print('Empate. Ninguém pontua')
    elif (jogador == 0 and computador == 2) or (jogador == 1 and computador == 0) or (jogador == 2 and computador == 1):
        print('O computador vence')
        placar_computador = placar_computador + 1
    else:
        print('O jogador vence')
        placar_jogador = placar_jogador + 1        

    print('')
    print('='*35)
    print('Jogar novamente? 0 - SIM | 1 - NÃO')
    if int(input()) == 1:
        break  