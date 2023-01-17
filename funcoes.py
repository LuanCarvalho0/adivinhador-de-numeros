import os


def iniciar_jogo():
    limpar_tela()
    print('-=' * 25)
    print('\t-> Adivinhe o Número <-')
    print('-=' * 25)
    print('Foi gerado um número entre 1 e 100...')


def quente_morno_frio(numero_chute, numero_aleatorio):
    if (numero_chute >= (numero_aleatorio - 10) and (numero_chute <= (numero_aleatorio + 10))):
        return vermelho('quente')
    elif (numero_chute >= (numero_aleatorio - 20) and (numero_chute <= (numero_aleatorio + 20))):
        return amarelo('morno')
    else:
        return azul('frio')


def limpar_tela():
    os.system('cls')

##### Funções de Colorir #####


def vermelho(texto):
    return f'\033[31m{texto}\033[0;0m'


def verde(texto):
    return f'\033[32m{texto}\033[0;0m'


def amarelo(texto):
    return f'\033[33m{texto}\033[0;0m'


def azul(texto):
    return f'\033[34m{texto}\033[0;0m'
