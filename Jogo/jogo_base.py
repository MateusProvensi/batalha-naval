from random import randint
from time import sleep
from os import system
import playsound

tem_barcos = True
continuar_a_jogar = ''
reiniciar_loop = True
continuar_obrigatoriamente_usuario = True
continuar_obrigatoriamente_pc = True
linha_coluna_usuario = ''
sentido = ''
pontos_usuario = pontos_pc = 0
tipos_barcos = ('P', 'S', 'B', 'N', 'C')
linha_coluna_barco_usuario = ''


def limpa_tela():
    system('cls')


def menu():
    while True:
        print('-=' * 20)
        print(
            '1 - Iniciar o jogo\n'
            '2 - Instruções\n'
            '3 - Sair'
        )
        print('-=' * 20)
        escolha = input('Digite sua opção: ')
        if escolha == '1':
            input('Pressione enter para iniciar')
            break
        elif escolha == '2':
            instrucoes()
        elif escolha == '3':
            print('Saindo...')
            sleep(2)
            exit()
        else:
            print('Digite algo válido.')


def instrucoes():
    print('\n1 - O jogo inicia com você adicionando seus barcos no tabuleiro, só será necessário que você digite a '
          'primeira casa do barco\n'
          '2 - Para dar um tiro no mar, será necessário que você digite primeiro a linha e depois a coluna, r'
          'espectivamente\n'
          '3 - Segue agora um informativo de quantas casa cada barco ocupa:\n'
          '    Porta aviões: 5 casas\n'
          '    Bote: 5 botes mas ocupam somente uma casa\n'
          '    Submarino: 3 casas\n'
          '    Navio: 4 casas\n'
          '    Cargueiro: 6 casas\n')


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


def definir_sentido():
    global sentido
    mostrar_tabuleiro_posicionamento_usuario()
    while True:
        sentido = input('Digite o sentido do seu barco [H/V]: ').strip().upper()
        if sentido not in ('H', 'V'):
            print('Seu sentido é inexistente.')
            continue
        else:
            if sentido == 'H':
                print('Você escolheu o sentido horizontal')
            else:
                print('Você escolheu o sentido vertical')
            break


def verificacao_linha_coluna_posicionamento_usuario(nome_do_barco: str, sigla_barco: str, min_linha: int,
                                                    max_linha: int, min_coluna: int, max_coluna: int, tamanho_barco: int):
    global linha_coluna_barco_usuario, reiniciar_loop, sentido
    while True:
        linha_coluna_barco_usuario = input(f'\nDigite a linha e a coluna, respectivamente, de onde ficará o '
                                           f'inicio do seu {nome_do_barco}: ').strip()
        if not linha_coluna_barco_usuario.isnumeric():
            print('Digite primeiro a linha e depois a coluna, números, por favor.')
            playsound.playsound('coordenadainexistente.m4a')
            sleep(1)
            continue
        elif len(linha_coluna_barco_usuario) != 2:
            print('Você digitou valores a mais ou a menos, hein')
            playsound.playsound('coordenadainexistente.m4a')
            sleep(1)
            continue
        else:
            if int(linha_coluna_barco_usuario[0]) > max_linha or int(linha_coluna_barco_usuario[0]) < min_linha:
                print('Se ele começar ai, cairá para fora do tabuleiro, tente outra linha')
                playsound.playsound('caminhoobstruido.m4a')
                sleep(1)
                continue
            if int(linha_coluna_barco_usuario[1]) > max_coluna or int(linha_coluna_barco_usuario[1]) < min_coluna:
                print('Se ele começar ai, cairá para fora do tabuleiro, tente outra coluna')
                playsound.playsound('caminhoobstruido.m4a')
                sleep(1)
                continue
            else:
                for i in range(tamanho_barco):
                    if tabuleiro_posicionamento_usuario[
                        int(linha_coluna_barco_usuario[0]) + (i if sentido == 'V' else 0)][
                        int(linha_coluna_barco_usuario[1]) + (i if sentido == 'H' else 0)] in \
                            tipos_barcos:
                        reiniciar_loop = True
                        break
                    elif i == tamanho_barco - 1:
                        reiniciar_loop = False
                        break
                if reiniciar_loop:
                    print('Existe um barco neste caminho, por favor, encontre outro.')
                    playsound.playsound('caminhoobstruido.m4a')
                    sleep(1)
                    continue
                else:
                    for i in range(tamanho_barco):
                        tabuleiro_posicionamento_usuario[
                            int(linha_coluna_barco_usuario[0]) + (i if sentido == 'V' else 0)][
                            int(linha_coluna_barco_usuario[1]) + (i if sentido == 'H' else 0)] = sigla_barco
                    break


def adicionando_porta_avioes_do_usuario():
    print('Agora é a vez do porta-aviões...')
    definir_sentido()
    if sentido == 'H':
        verificacao_linha_coluna_posicionamento_usuario('porta aviões', 'P', 0, 9, 0, 5, 5)
    else:
        verificacao_linha_coluna_posicionamento_usuario('porta aviões', 'P', 0, 5, 0, 9, 5)


def adicionando_botes_do_usuario():
    global linha_coluna_barco_usuario
    print('\nAgora é a vez dos botes...')
    numero_bote = 1
    while True:
        mostrar_tabuleiro_posicionamento_usuario()
        linha_coluna_barco_usuario = input(f'\nDigite a linha e a coluna, respectivamente, de onde ficará o seu '
                                           f'{numero_bote}º Bote: ').strip()
        if not linha_coluna_barco_usuario.isnumeric():
            print('Digite primeiro a linha e depois a coluna, números, por favor.')
            playsound.playsound('coordenadainexistente.m4a')
            sleep(0.5)
            continue
        elif len(linha_coluna_barco_usuario) != 2:
            print('Você digitou valores a mais ou a menos, hein')
            playsound.playsound('coordenadainexistente.m4a')
            sleep(0.5)
            continue
        else:
            if tabuleiro_posicionamento_usuario[int(linha_coluna_barco_usuario[0])][int(
                    linha_coluna_barco_usuario[1])] in tipos_barcos:
                print('Esse lugar já está ocupado, tente outro.')
                playsound.playsound('caminhoobstruido.m4a')
                sleep(1)
                continue
            else:
                tabuleiro_posicionamento_usuario[int(linha_coluna_barco_usuario[0])][int(
                    linha_coluna_barco_usuario[1])] = 'B'
                numero_bote += 1
                if numero_bote == 6:
                    break


def adicionando_submarino_do_usuario():
    limpa_tela()
    print('Agora é a vez do submarino...')
    definir_sentido()
    if sentido == 'H':
        verificacao_linha_coluna_posicionamento_usuario('submarino', 'S', 0, 9, 0, 7, 3)
    else:
        verificacao_linha_coluna_posicionamento_usuario('submarino', 'S', 0, 7, 0, 9, 3)


def adicionando_navio_do_usuario():
    limpa_tela()
    print('Agora é a vez do navio...')
    definir_sentido()
    if sentido == 'H':
        verificacao_linha_coluna_posicionamento_usuario('navio', 'N', 0, 9, 0, 6, 4)
    else:
        verificacao_linha_coluna_posicionamento_usuario('navio', 'N', 0, 6, 0, 9, 4)


def adicionando_cargueiro_do_usuario():
    limpa_tela()
    print('Agora é a vez do seu cargueiro...')
    definir_sentido()
    if sentido == 'H':
        verificacao_linha_coluna_posicionamento_usuario('cargueiro', 'C', 0, 9, 0, 4, 6)
    else:
        verificacao_linha_coluna_posicionamento_usuario('cargueiro', 'C', 0, 4, 0, 9, 6)


def mostrar_tabuleiro_posicionamento_usuario():
    print(
        '    0 1 2 3 4 5 6 7 8 9\n'
        '    ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓'
    )
    for linha_posicionamento in range(10):
        print(linha_posicionamento, end=' → ')
        for coluna_posicionamento in range(10):
            print(tabuleiro_posicionamento_usuario[linha_posicionamento][coluna_posicionamento], end=' ')
        print()


def mostra_tabuleiro_usuario():
    print(
        '    0 1 2 3 4 5 6 7 8 9\n'
        '    ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓'
    )
    for linha_mostrando_usuario in range(10):
        print(linha_mostrando_usuario, end=' → ')
        for coluna_mostrando_usuario in range(10):
            print(tabuleiro_pc_mostrar_usuario[linha_mostrando_usuario][coluna_mostrando_usuario], end=' ')
        print()


def receber_verificar_jogada_usuario():
    global linha_coluna_usuario
    while True:
        while True:
            linha_coluna_usuario = input('\nDigite a linha e a coluna, respectivamente, para acertar um barco '
                                         'inimigo: ').strip()
            if not linha_coluna_usuario.isnumeric():
                print('Digite primeiro a linha e depois a coluna, números, por favor.')
                playsound.playsound('coordenadainexistente.m4a')
                continue
            elif len(linha_coluna_usuario) != 2:
                print('Você digitou valores a mais ou a menos, hein')
                playsound.playsound('coordenadainexistente.m4a')
                continue
            else:
                break

        if tabuleiro_back[int(linha_coluna_usuario[0])][int(linha_coluna_usuario[1])] in ('█', 'X'):
            print('Você já jogou neste lugar, escolha outro.')
            playsound.playsound('coordenadaatingida.m4a')
            continue
        else:
            break


def verificando_se_ha_barcos_separadamente(sigla_barco, nome_barco):
    global tem_barcos
    for linha_verificacao in tabuleiro_back:
        if sigla_barco in linha_verificacao:
            print(f'Ainda há pedaços do {nome_barco}.')
            tem_barcos = True
            break
        else:
            tem_barcos = False
    if not tem_barcos:
        print(f'O {nome_barco} foi destruído por completo')


def adicionar_tabuleiro():
    tabuleiro_back[int(linha_coluna_usuario[0])][int(linha_coluna_usuario[1])] = 'X'
    tabuleiro_pc_mostrar_usuario[int(linha_coluna_usuario[0])][int(linha_coluna_usuario[1])] = 'X'


def verificar_se_acertou():
    global continuar_obrigatoriamente_usuario, pontos_usuario, tem_barcos
    if tabuleiro_back[int(linha_coluna_usuario[0])][int(linha_coluna_usuario[1])] in tipos_barcos:
        if tabuleiro_back[int(linha_coluna_usuario[0])][int(linha_coluna_usuario[1])] == 'P':
            print('BOOOOM. Acertou um porta aviões!')
            playsound.playsound('pinimigo.m4a')
            adicionar_tabuleiro()
            verificando_se_ha_barcos_separadamente('P', 'porta aviões')

        elif tabuleiro_back[int(linha_coluna_usuario[0])][int(linha_coluna_usuario[1])] == 'N':
            print('BOOOOM. Acertou um navio!')
            playsound.playsound('ninimigo.m4a')
            adicionar_tabuleiro()
            verificando_se_ha_barcos_separadamente('N', 'navio')

        elif tabuleiro_back[int(linha_coluna_usuario[0])][int(linha_coluna_usuario[1])] == 'B':
            print('BOOOOM. Acertou um bote!')
            playsound.playsound('binimigo.m4a')
            adicionar_tabuleiro()
            verificando_se_ha_barcos_separadamente('B', 'bote')

        elif tabuleiro_back[int(linha_coluna_usuario[0])][int(linha_coluna_usuario[1])] == 'S':
            print('BOOOOM. Acertou um submarino!')
            playsound.playsound('sinimigo.m4a')
            adicionar_tabuleiro()
            verificando_se_ha_barcos_separadamente('S', 'submarino')

        elif tabuleiro_back[int(linha_coluna_usuario[0])][int(linha_coluna_usuario[1])] == 'C':
            print('BOOOOM. Acertou um cargueiro!')
            playsound.playsound('cinimigo.m4a')
            adicionar_tabuleiro()
            verificando_se_ha_barcos_separadamente('C', 'cargueiro')
        sleep(1)
        pontos_usuario += 1

    else:
        print('BOOOOM... na água.')
        tabuleiro_pc_mostrar_usuario[int(linha_coluna_usuario[0])][int(linha_coluna_usuario[1])] = '█'
        tabuleiro_back[int(linha_coluna_usuario[0])][int(linha_coluna_usuario[1])] = '█'
        playsound.playsound('tiroagua.m4a')
        sleep(0.5)
    if pontos_usuario == 23:
        print('\nParabéns, você ganhouu!!\n')
        continuar_obrigatoriamente_usuario = False
    else:
        continuar_obrigatoriamente_usuario = True


def jogada_pc():
    global pontos_pc, continuar_obrigatoriamente_pc
    while True:
        linha_pc = randint(0, 9)
        coluna_pc = randint(0, 9)
        if tabuleiro_posicionamento_usuario[linha_pc][coluna_pc] in ('X', '█'):
            continue
        print(f'O PC jogou na linha {linha_pc} e coluna {coluna_pc}...')
        sleep(1)
        if tabuleiro_posicionamento_usuario[linha_pc][coluna_pc] in tipos_barcos:
            if tabuleiro_posicionamento_usuario[linha_pc][coluna_pc] == 'P':
                print('BOOOM... o pc acertou um porta aviões.')
                playsound.playsound('paliado.m4a')
            elif tabuleiro_posicionamento_usuario[linha_pc][coluna_pc] == 'B':
                print('BOOOM... o pc acertou um bote.')
                playsound.playsound('baliado.m4a')
            elif tabuleiro_posicionamento_usuario[linha_pc][coluna_pc] == 'S':
                print('BOOOM... o pc acertou um submarino.')
                playsound.playsound('saliado.m4a')
            elif tabuleiro_posicionamento_usuario[linha_pc][coluna_pc] == 'N':
                print('BOOOM... o pc acertou um navio.')
                playsound.playsound('naliado.m4a')
            elif tabuleiro_posicionamento_usuario[linha_pc][coluna_pc] == 'C':
                print('BOOOM... o pc acertou um cargueiro.')
                playsound.playsound('caliado.m4a')
            tabuleiro_posicionamento_usuario[linha_pc][coluna_pc] = 'X'
            sleep(0.5)
            pontos_pc += 1
            if pontos_pc == 23:
                print('Que pena, você perdeu! Tente novamente')
                sleep(1)
                continuar_obrigatoriamente_pc = False
            break
        else:
            tabuleiro_posicionamento_usuario[linha_pc][coluna_pc] = '█'
            print('BOOOM... na água')
            playsound.playsound('tiroagua.m4a')
            sleep(0.5)
            break


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
    menu()
    limpa_tela()
    tabuleiro_back = []
    tabuleiro_pc_mostrar_usuario = []
    tabuleiro_posicionamento_usuario = []

    for linha in range(10):
        tabuleiro_back.append([])
        tabuleiro_pc_mostrar_usuario.append([])
        tabuleiro_posicionamento_usuario.append([])

        for coluna in range(10):
            tabuleiro_back[linha].append('A')
            tabuleiro_pc_mostrar_usuario[linha].append('*')
            tabuleiro_posicionamento_usuario[linha].append('*')

    definir_porta_avioes()
    definir_botes()
    definir_submarino()
    definir_navio()
    definir_cargueiro()
    if True:
        print('Antes de tudo, vamos definir onde ficarão os seus barcos.\n')
        playsound.playsound('definirbarcos.m4a')
        adicionando_porta_avioes_do_usuario()
        adicionando_botes_do_usuario()
        adicionando_submarino_do_usuario()
        adicionando_navio_do_usuario()
        adicionando_cargueiro_do_usuario()
        print('Seu tabuleiro ficou da seguinte forma:\n')
        mostrar_tabuleiro_posicionamento_usuario()
        sleep(1)
        print('Preparado?')
        playsound.playsound('preparado.m4a')
        print('3')
        playsound.playsound('tres.m4a')
        print('2')
        playsound.playsound('dois.m4a')
        print('1')
        playsound.playsound('um.m4a')
        print('BATALHA!')
        playsound.playsound('batalha.m4a')
        while True:
            limpa_tela()
            print('Aqui está seu tabuleiro: \n')
            mostrar_tabuleiro_posicionamento_usuario()
            print('-=' * 25)
            print('Aqui está o tabuleiro do PC: \n')
            mostra_tabuleiro_usuario()
            print('-=' * 25)
            receber_verificar_jogada_usuario()
            print()
            verificar_se_acertou()
            print()
            print('Agora é a vez do PC: ')
            jogada_pc()
            if continuar_obrigatoriamente_usuario and continuar_obrigatoriamente_pc:
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
