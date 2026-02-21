# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
#qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
n = int(input("Digite um Número (de 1 a 5): "))
nu = randint(0,5)
print('PROCESSANDO...')
sleep(3)
if n == nu:
    print('PARABÉNS! Você conseguiu me vencer!!!')
else:
    print('Não foi desta vez :(')