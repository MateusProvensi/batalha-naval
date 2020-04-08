from random import randint
from time import sleep
from os import system

continuar = True


def limpa_tela():
    system('cls')


tabuleiro_back = [
    ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'],
    ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'],
    ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'],
    ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'],
    ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'],
    ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'],
    ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'],
    ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'],
    ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'],
    ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'],
    ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'],
    ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'],
    ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'],
    ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'],
    ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A']
]

tabuleiro_usuario = [
    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*']
]

contador = 0
while True:
    linha = randint(1, 15)
    coluna = randint(1, 15)
    if tabuleiro_back[coluna - 1][linha - 1] == 'N':
        continue
    else:
        tabuleiro_back[coluna - 1][linha - 1] = 'N'
        contador += 1
    if contador == 100:
        break

# tabuleiro_back[coluna - 1][linha - 1] = 'N'
# tabuleiro_back[coluna if coluna < 4 else coluna - 2][linha - 1] = 'N'
# tabuleiro_back[coluna + 1 if coluna + 1 <= 4 else coluna - 3 if coluna - 3 > - 1 else coluna][linha - 1] = 'N'

while continuar:
    limpa_tela()
    for coluna_mostrar in range(0, 15):
        for linha_mostrar in range(0, 15):
            print(f'{tabuleiro_usuario[linha_mostrar][coluna_mostrar]}', end=' ')
        print()

    jogada_coluna = input('Digite a coluna da sua jogada: ')

    if not jogada_coluna.isnumeric():
        print('Digite um número.')
    if int(jogada_coluna) > 15 or int(jogada_coluna) <= 0:
        print('Digite uma coluna válida')
        sleep(1)
        continue

    jogada_linha = input('Digite a linha da sua jogada: ')

    if int(jogada_linha) > 15 or int(jogada_linha) <= 0:
        print('Digite uma linha válida')
        sleep(2)
        continue

    if tabuleiro_back[int(jogada_coluna) - 1][int(jogada_linha) - 1] == 'N':
        tabuleiro_usuario[int(jogada_coluna) - 1][int(jogada_linha) - 1] = 'X'
        print('Acertou um Navio!!!')
        for coluna_mostrar in range(0, 15):
            for linha_mostrar in range(0, 15):
                print(f'{tabuleiro_usuario[linha_mostrar][coluna_mostrar]}', end=' ')
            print()
        sleep(2)
    else:
        tabuleiro_usuario[int(jogada_coluna) - 1][int(jogada_linha) - 1] = '#'
        print('Foi no mar!!!')
        for coluna_mostrar in range(0, 15):
            for linha_mostrar in range(0, 15):
                print(f'{tabuleiro_usuario[linha_mostrar][coluna_mostrar]}', end=' ')
            print()
        sleep(1)

    for coluna_mostrar in range(0, 15):
        for linha_mostrar in range(0, 15):
            if tabuleiro_usuario[linha_mostrar][coluna_mostrar] == 'N':
                continuar = True

    if not continuar:
        break
