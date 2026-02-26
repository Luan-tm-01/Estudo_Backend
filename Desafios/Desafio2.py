# Jogo de Par ou Ímpar
from random import randint
from time import sleep

g = 0
print('=-'*15)
print('VAMOS JOGAR PAR OU ÍMPAR')
while True:
    c = randint(0,10)
    print('=-' * 15)
    v = int(input('Diga um valor: '))
    t = c + v
    p = ' '
    while p not in 'PI':
        p = str(input('Par ou Ímpar [P/I]? ')).upper()[0]
    print('=-'*15)
    if t % 2 == 0:
        print(f'Você jogou {v} e o computador {c}. Total de {t} DEU PAR')
    else:
        print(f'Você jogou {v} e o computador {c}. Total de {t} DEU ÍMPAR')
    print('=-' * 15)
    if p == "P" and t % 2 == 0:
        print('Você VENCEU!\nVamos jogar novamente...')
        sleep(1)
        g += 1
    elif p == "I" and t % 2 != 0:
        print('Você VENCEU!\nVamos jogar novamente...')
        sleep(1)
        g += 1
    elif p == "P" and t % 2 != 0:
        print(f'Você PERDEU!\nGAME OVER! Você venceu {g} vezes.')
        sleep(1)
        break
    elif p == "I" and t % 2 == 0:
        print(f'Você PERDEU!\nGAME OVER! Você venceu {g} vezes.')
        sleep(1)
        break
