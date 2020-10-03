from csv import reader, DictReader
import pygame
import os
from random import randint

pygame.mixer.init()
pygame.init()

with open('musicas/bd.csv') as arq:
    tamanho = 0
    arquivo = reader(arq)
    next(arquivo)
    for linha in arquivo:
        tamanho += 1


def checa_musicas():
    with open('musicas/bd.csv') as arq:
        arquivo = reader(arq)
        next(arquivo)
        for linha in arquivo:
            print(f'Id: {linha[0]}, Banda: {linha[1]}, Musica: {linha[2]}, Album:{linha[3]}, Genero:{linha[4]},'
                  f' Duração:{linha[5]}.')


def reproduz_musica(idmusica):
    with open('musicas/bd.csv') as arq:
        dic = DictReader(arq)
        for linha in dic:
            if linha['id'] == f'{idmusica}':
                musica = linha['nome']
    nomemusica = f'{idmusica}.mp3'
    if os.path.exists(f'musicas/{nomemusica}'):
        print(f'Você está reproduzindo: {musica}')
        pygame.mixer.music.load(f'musicas/{idmusica}.mp3')
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(1)

        duracao = pygame.time.Clock()
        duracao.tick(10)

        while pygame.mixer.music.get_busy():
            pygame.event.poll()
            duracao.tick(10)

            selecao = input('+: Aumentar Volume/ -: Abaixar Volume/ 0: sair')
            if selecao == '+':
                volume = pygame.mixer.music.get_volume()
                pygame.mixer.music.set_volume(volume + 0.1)
            elif selecao == '-':
                volume = pygame.mixer.music.get_volume()
                pygame.mixer.music.set_volume(volume - 0.1)
            elif selecao == '0':
                pygame.mixer.music.stop()
                break

    else:
        print('Não reconhecemos esse ID, por favor, informe outro.')


print('Bem-vindo ao Spotifu$#')
print('Selecione uma das seguintes opções:')

while True:
    print('1- Checar as músicas do sistema.')
    print('2- Reproduzir determinada música.')
    print('3- Sair')

    escolha = input()
    if escolha == '1':
        checa_musicas()
    elif escolha == '2':
        idm = input('Digite o Id da música desejada ou S para ShufflePlay: ')
        if idm == 'S' or idm == 's':
            idm = str(randint(0, tamanho))
        reproduz_musica(idm)
    elif escolha == '3':
        break
    else:
        print('Valor Inválido.')
