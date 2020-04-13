from random import randint
from time import sleep
from os import system

continuar = True
reiniciar_loop = True


def limpa_tela():
    system('cls')


def definir_porta_avioes():
    linha_porta_avioes = randint(0, 4)
    coluna_porta_avioes = randint(0, 9)
    for i in range(5):
        tabuleiro_back[linha_porta_avioes + i][coluna_porta_avioes] = 'P'


def definir_botes():
    for i in range(5):
        linha_bote_atual = randint(0, 9)
        coluna_bote_atual = randint(0, 9)
        while tabuleiro_back[linha_bote_atual][coluna_bote_atual] in ('P', 'S', 'B', 'N'):
            linha_bote_atual = randint(0, 9)
            coluna_bote_atual = randint(0, 9)
        tabuleiro_back[linha_bote_atual][coluna_bote_atual] = 'B'


def definir_submarino():
    global reiniciar_loop
    while True:
        linha_submarino = randint(0, 7)
        coluna_submarino = randint(0, 9)
        for i in range(3):
            if tabuleiro_back[linha_submarino + i][coluna_submarino] in ('P', 'S', 'B', 'N'):
                reiniciar_loop = True
                break
            elif i == 2:
                reiniciar_loop = False
                break
        if reiniciar_loop:
            continue
        else:
            for i in range(3):
                tabuleiro_back[linha_submarino + i][coluna_submarino] = 'S'
            break


def definir_navio():
    global reiniciar_loop
    while True:
        linha_navio = randint(0, 9)
        coluna_navio = randint(0, 6)
        for i in range(4):
            if tabuleiro_back[linha_navio][coluna_navio + i] in ('P', 'S', 'B', 'N'):
                reiniciar_loop = True
                break
            elif i == 3:
                reiniciar_loop = False
                break
        if reiniciar_loop:
            continue
        else:
            for i in range(4):
                tabuleiro_back[linha_navio][coluna_navio + i] = 'N'
            break


def definir_cargueiro():
    global reiniciar_loop
    while True:
        linha_cargueiro = randint(0, 9)
        coluna_cargueiro = randint(0, 4)
        for i in range(6):
            if tabuleiro_back[linha_cargueiro][coluna_cargueiro + i] in ('P', 'S', 'B', 'N'):
                reiniciar_loop = True
                break
            elif i == 5:
                reiniciar_loop = False
                break
        if reiniciar_loop:
            continue
        else:
            for i in range(6):
                tabuleiro_back[linha_cargueiro][coluna_cargueiro + i] = 'C'
            break


tabuleiro_back = []
tabuleiro_usuario = []

for linha in range(10):
    tabuleiro_back.append([])
    tabuleiro_usuario.append([])
    for coluna in range(10):
        tabuleiro_back[linha].append(';')
        tabuleiro_usuario[linha].append('#')

definir_porta_avioes()
definir_botes()
definir_submarino()

definir_navio()

definir_cargueiro()

for l in range(10):
    for c in range(10):
        print(tabuleiro_back[l][c], end=' ')
    print()
print('-=' * 25)
