from random import randint
from time import sleep
from os import system

continuar_a_jogar = ''
reiniciar_loop = True
continuar_obrigatoriamente = linha_usuario = coluna_usuario = 0
tipos_barcos = ('P', 'S', 'B', 'N')


def limpa_tela():
    system('cls')


def definir_porta_avioes():
    global reiniciar_loop
    while True:
        linha_porta_avioes = randint(0, 4)
        coluna_porta_avioes = randint(0, 9)
        for i in range(5):
            if tabuleiro_back[linha_porta_avioes + i][coluna_porta_avioes] in tipos_barcos:
                reiniciar_loop = True
                break
            elif i == 4:
                reiniciar_loop = False
                break
        if reiniciar_loop:
            continue
        else:
            for i in range(3):
                tabuleiro_back[linha_porta_avioes + i][coluna_porta_avioes] = 'P'
            break


def definir_botes():
    for i in range(5):
        linha_bote_atual = randint(0, 9)
        coluna_bote_atual = randint(0, 9)
        while tabuleiro_back[linha_bote_atual][coluna_bote_atual] in tipos_barcos:
            linha_bote_atual = randint(0, 9)
            coluna_bote_atual = randint(0, 9)
        tabuleiro_back[linha_bote_atual][coluna_bote_atual] = 'B'


def definir_submarino():
    global reiniciar_loop
    while True:
        linha_submarino = randint(0, 7)
        coluna_submarino = randint(0, 9)
        for i in range(3):
            if tabuleiro_back[linha_submarino + i][coluna_submarino] in tipos_barcos:
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
            if tabuleiro_back[linha_navio][coluna_navio + i] in tipos_barcos:
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
            if tabuleiro_back[linha_cargueiro][coluna_cargueiro + i] in tipos_barcos:
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


def mostra_tabuleiro_no_teste():
    for linha_teste in range(10):
        for coluna_teste in range(10):
            print(tabuleiro_back[linha_teste][coluna_teste], end=' ')
        print()


def mostra_tabuleiro_usuario():
    for linha_mostrando_usuario in range(10):
        for coluna_mostrando_usuario in range(10):
            print(tabuleiro_usuario[linha_mostrando_usuario][coluna_mostrando_usuario], end=' ')
        print()


def receber_verificar_jogada_usuario():
    global linha_usuario, coluna_usuario
    while True:
        while True:
            try:
                linha_usuario = int(input('\nDigite a linha, começa em 1: ')) - 1
            except ValueError:
                print('Digite um número inteiro, por favor.')
                continue
            if linha_usuario > 10 or linha_usuario < 1:
                print('Digite uma linha válida.')
            else:
                break
        while True:
            try:
                coluna_usuario = int(input('\nDigite a coluna, começa em 1: ')) - 1
            except ValueError:
                print('Digite um número inteiro, por favor.')
                continue
            if coluna_usuario > 10 or coluna_usuario < 1:
                print('Digite uma coluna válida.')
            else:
                break
        if tabuleiro_back[linha_usuario][coluna_usuario] in ('█', 'X'):
            print('Você já jogou neste lugar, escolha outro.')
            continue
        else:
            break


def verificar_se_acertou():
    global continuar_obrigatoriamente
    if tabuleiro_back[linha_usuario][coluna_usuario] in tipos_barcos:
        if tabuleiro_back[linha_usuario][coluna_usuario] == 'P':
            print('BOOOOM. Acertou um porta aviões!')
        elif tabuleiro_back[linha_usuario][coluna_usuario] == 'N':
            print('BOOOOM. Acertou um návio!')
        elif tabuleiro_back[linha_usuario][coluna_usuario] == 'B':
            print('BOOOOM. Acertou um bote!')
        elif tabuleiro_back[linha_usuario][coluna_usuario] == 'S':
            print('BOOOOM. Acertou um submarino!')
        sleep(2)
        tabuleiro_back[linha_usuario][coluna_usuario] = 'X'
        tabuleiro_usuario[linha_usuario][coluna_usuario] = 'X'
    else:
        print('BOOOOM... na água.')
        tabuleiro_usuario[linha_usuario][coluna_usuario] = '█'
        tabuleiro_back[linha_usuario][coluna_usuario] = '█'
        sleep(2)
    for linha_verificacao_vitoria in range(10):
        for coluna_verificacao_vitoria in range(10):
            if tabuleiro_back[linha_verificacao_vitoria][coluna_verificacao_vitoria] in tipos_barcos:
                continuar_obrigatoriamente += 1
                break
    print('Parabéns, você ganhouu!!')


def continuar_jogar():
    global continuar_a_jogar
    continuar_a_jogar = input('Deseja continuar jogando[S/N]? ').strip().upper()
    while continuar_a_jogar not in ('S', 'N'):
        print('Somente S ou N.')
        continuar_a_jogar = input('\nDeseja continuar jogando[S/N]? ').strip().upper()
    if continuar_a_jogar == 'S':
        continuar_a_jogar = True
    else:
        continuar_a_jogar = False


while True:
    limpa_tela()
    tabuleiro_back = []
    tabuleiro_usuario = []

    for linha in range(10):
        tabuleiro_back.append([])
        tabuleiro_usuario.append([])
        for coluna in range(10):
            tabuleiro_back[linha].append('A')
            tabuleiro_usuario[linha].append('#')

    definir_porta_avioes()
    definir_botes()
    definir_submarino()
    definir_navio()
    definir_cargueiro()

    while True:
        mostra_tabuleiro_no_teste()
        print('-=' * 25)
        mostra_tabuleiro_usuario()
        print('-=' * 25)
        receber_verificar_jogada_usuario()
        print()
        verificar_se_acertou()
        if continuar_obrigatoriamente:
            continue
        else:
            continuar_jogar()
    if continuar_a_jogar:
        print('\nQue bom que jogará mais!!! Pressione enter para continuar.')
        input()
    else:
        print('\nPor que nos abandonaste... :(')
        sleep(2)
