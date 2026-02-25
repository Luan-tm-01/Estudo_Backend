# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n = int(input('Digite um número: '))
d = 0
for i in range (1, n+1):
    if n % i == 0:
        print(f'\033[33m{i}', end=" ")
        d += 1
    else:
        print(f'\033[31m{i}', end=" ")
print(f'\n\033[mO número {n} foi divisível {d} vezes')
if d > 2:

    print('E por isso ele NÃO É PRIMO!')
else:
    print('E por isso ele PRIMO!')