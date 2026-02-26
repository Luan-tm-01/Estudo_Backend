# Lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
print('Gerador de PA')
print('-'*20)
t = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
ri = 0
n = 10
while n != 0:
    print(t+ri, end=" -> ")
    ri += r
    n -= 1
print(end="FIM")