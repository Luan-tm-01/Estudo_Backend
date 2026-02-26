# Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

v = 0
n = 0
while v != 999:
    o = int(input('Digite um valor (999 para parar): '))
    if o == 999:
        break
    v += o
    n += 1
print(f'A soma dos {n} valores foi {v}!')

