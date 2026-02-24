# Crie um programa que faça o computador jogar Jokenpô com você.
from random import choice
from time import sleep

o = ['Pedra','Papel', 'Tesoura']
o = choice(o)
print('Suas opções:\n[ 0 ] PEDRA\n[ 1 ] PAPEL\n[ 2 ] TESOURA')
j = int(input(f'Qual é a sua jogada? '))
if j == 0:
    j = str('Pedra')
if j == 1:
    j = str('Papel')
if j == 2:
    j = str('Tesoura')
sleep(0.5)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')
sleep(0.5)
print('-=-'*12)
print(f'Computador jogou {o}\nJogador jogou {j}')
print('-=-'*12)
if j == 'Pedra' and o == 'Papel':
    print('COMPUTADOR VENCE')
elif j == 'Papel' and o == 'Papel':
    print('EMPATE')
elif j == 'Tesoura' and o == 'Papel':
    print('JOGADOR VENCE')
elif j == 'Pedra' and o == 'Pedra':
    print('EMPATE')
elif j == 'Papel' and o == 'Pedra':
    print('JOGADOR VENCE')
elif j == 'Tesoura' and o == 'Pedra':
    print('COMPUTADOR VENCE')
elif j == 'Pedra' and o == 'Tesoura':
    print('JOGADOR VENCE')
elif j == 'Papel' and o == 'Tesoura':
    print('COMPUTADOR VENCE')
elif j == 'Tesoura' and o == 'Tesoura':
    print('EMPATE')
