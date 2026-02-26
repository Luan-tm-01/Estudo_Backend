# Perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
print('Gerador de PA')
print('-'*20)
t = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
ri = 0
n = 11
while n != 0:
    if n != 1:
        print(t+ri, end=" -> ")
        ri += r
    elif n == 0:
        print(end="PAUSA")
        n = int(input('\nQuantos termos você quer mostrar a mais? ')) + 1
    n -= 1



