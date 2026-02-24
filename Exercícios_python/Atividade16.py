# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais

pn = int(input('Primeiro número: '))
sn = int(input('Segundo número: '))

if pn > sn:
    print('O PRIMEIRO número é maior!')
elif pn < sn:
    print('O SEGUNDO número é maior!')
elif pn == sn:
    print('Os dois valores são IGUAIS!')