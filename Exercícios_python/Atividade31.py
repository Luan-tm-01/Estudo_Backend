# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
from time import sleep

print('Sou seu computador...')
sleep(1)
n = randint(0,10)
print('Acabei de pensar em um número entre 0 e 10.\nSerá que você consegue adivinhar qual foi?')
sleep(1)
p = int(input('Qual é seu palpite? '))
t = 0
sleep(1)
while p != n:
    if p < n:
        print('Mais... Tente mais uma vez')
        p = int(input('Qual é seu palpite? '))
        t += 1
    elif p > n:
        print('Menos... Tente mais uma vez')
        p = int(input('Qual é seu palpite? '))
        t += 1
if t == 0:
    print('Parabéns, Você acertou de PRIMEIRA')
elif t == 1:
    print(f'Acertou com {t} tentativa. Parabéns!')
else:
    print(f'Acertou com {t} tentativas. Parabéns!')
