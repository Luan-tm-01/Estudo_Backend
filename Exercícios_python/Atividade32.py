# Faça um programa que leia um número qualquer e mostre o seu fatorial.

n = int(input('Digite um número para\nCalcular seu Fatorial: '))
f = 1
print(f'Calculando {n}! =',end=' ')
while n > 0:
    f *= n
    if n == 1:
        print(n, end=' ')
    elif n != 1:
        print(n, end=' X ')
    n -= 1
print(f'= {f}')




