from random import randint
from time import sleep
from os import system

tem_barcos = True
continuar_a_jogar = ''
reiniciar_loop = True
continuar_obrigatoriamente = True
linha_coluna_usuario = pontos_usuario = 0
tipos_barcos = ('P', 'S', 'B', 'N', 'C')


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
            for i in range(5):
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
    global linha_coluna_usuario
    while True:
        while True:
            linha_coluna_usuario = input('\nDigite a linha e a coluna, respectivamente, começa em 0: ').strip()
            if not linha_coluna_usuario.isnumeric():
                print('Digite primeiro a linha e depois a coluna, números, por favor.')
                continue
            elif len(linha_coluna_usuario) != 2:
                print('Você digitou valores a mais ou a menos, hein')
                continue
            else:
                break

        if tabuleiro_back[int(linha_coluna_usuario[0])][int(linha_coluna_usuario[1])] in ('█', 'X'):
            print('Você já jogou neste lugar, escolha outro.')
            continue
        else:
            break


def verificando_se_ha_barcos_separadamente(silha_barco, nome_barco):
    global tem_barcos
    for linha_verificacao in tabuleiro_back:
        if silha_barco in linha_verificacao:
            print(f'Ainda há pedaços do {nome_barco}.')
            tem_barcos = True
            break
        else:
            tem_barcos = False
    if not tem_barcos:
        print(f'O {nome_barco} foi destruído por completo')


def adicionar_tabuleiro():
    tabuleiro_back[int(linha_coluna_usuario[0])][int(linha_coluna_usuario[1])] = 'X'
    tabuleiro_usuario[int(linha_coluna_usuario[0])][int(linha_coluna_usuario[1])] = 'X'


def verificar_se_acertou():
    global continuar_obrigatoriamente, pontos_usuario, tem_barcos
    if tabuleiro_back[int(linha_coluna_usuario[0])][int(linha_coluna_usuario[1])] in tipos_barcos:
        if tabuleiro_back[int(linha_coluna_usuario[0])][int(linha_coluna_usuario[1])] == 'P':
            print('BOOOOM. Acertou um porta aviões!')
            adicionar_tabuleiro()
            verificando_se_ha_barcos_separadamente('P', 'porta aviões')

        elif tabuleiro_back[int(linha_coluna_usuario[0])][int(linha_coluna_usuario[1])] == 'N':
            print('BOOOOM. Acertou um navio!')
            adicionar_tabuleiro()
            verificando_se_ha_barcos_separadamente('N', 'navio')

        elif tabuleiro_back[int(linha_coluna_usuario[0])][int(linha_coluna_usuario[1])] == 'B':
            print('BOOOOM. Acertou um bote!')
            adicionar_tabuleiro()
            verificando_se_ha_barcos_separadamente('B', 'bote')

        elif tabuleiro_back[int(linha_coluna_usuario[0])][int(linha_coluna_usuario[1])] == 'S':
            print('BOOOOM. Acertou um submarino!')
            adicionar_tabuleiro()
            verificando_se_ha_barcos_separadamente('S', 'submarino')

        elif tabuleiro_back[int(linha_coluna_usuario[0])][int(linha_coluna_usuario[1])] == 'C':
            print('BOOOOM. Acertou um cargueiro!')
            adicionar_tabuleiro()
            verificando_se_ha_barcos_separadamente('C', 'cargueiro')
        sleep(3)
        pontos_usuario += 1

    else:
        print('BOOOOM... na água.')
        tabuleiro_usuario[int(linha_coluna_usuario[0])][int(linha_coluna_usuario[1])] = '█'
        tabuleiro_back[int(linha_coluna_usuario[0])][int(linha_coluna_usuario[1])] = '█'
        sleep(3)
    if pontos_usuario == 23:
        print('\nParabéns, você ganhouu!!\n')
        continuar_obrigatoriamente = False
    else:
        continuar_obrigatoriamente = True


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
    print()
    tabuleiro_back = []
    tabuleiro_usuario = []

    for linha in range(10):
        tabuleiro_back.append([])
        tabuleiro_usuario.append([])
        for coluna in range(10):
            tabuleiro_back[linha].append('A')
            tabuleiro_usuario[linha].append('*')

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
            break
    continuar_jogar()
    if continuar_a_jogar:
        print('\nQue bom que jogará mais!!! Pressione enter para continuar.')
        input()
    else:
        print('\nPor que nos abandonaste... :(')
        sleep(2)
