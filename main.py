from funcoes import *
from random import randint


while True:
    limpar_tela()
    input(amarelo('Aperte qualquer tecla para começar...'))
    iniciar_jogo()

    numero_aleatorio = randint(1, 100)
    quantidade_chute = 0
    while True:
        try:
            numero_chute = int(input('Chute um número: '))
            quantidade_chute += 1
            if numero_chute == numero_aleatorio:
                print(
                    verde(f'PARABÉNS! VOCÊ CHUTOU O VALOR CERTO: {numero_aleatorio}'))
                print(amarelo(f'Quantidade de chutes: {quantidade_chute}'))
                break
            elif numero_chute > numero_aleatorio:
                print(
                    f'Você esta {quente_morno_frio(numero_chute, numero_aleatorio)}, chute um número menor')
            elif numero_chute < numero_aleatorio:
                print(
                    f'Você esta {quente_morno_frio(numero_chute, numero_aleatorio)}, chute um número maior')
        except:
            print(vermelho('Por favor digitar apenas número inteiro!'))

    opcao = input('Jogo encerrado, gostaria de jogar novamente?[s/n] ').lower()
    if opcao == 'n':
        print('-' * 30)
        print(vermelho('Encerrando o jogo...'))
        print('-' * 30)
        input(amarelo('Aperte qualquer tecla para continuar...'))
        exit()
