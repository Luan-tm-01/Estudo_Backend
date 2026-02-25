# Calculadora
from math import sqrt
from time import sleep

print ('-=-'*10)
print('          Calculadora')
print ('-=-'*10)
pn = int(input('Primeiro valor: '))
sn = int(input('Segundo valor: '))
o = 0
n = 0
while o != 7:
    print('    [ 1 ] Somar\n    [ 2 ] Subtração\n    [ 3 ] Multiplicação\n    [ 4 ] Divisão\n    [ 5 ] Raiz Quadrada\n    [ 6 ] Potenciação\n    [ 7 ] Sair do Programa\n')
    o = int(input('>>>>> Qual é a sua opção? '))
    print('\033[m-=-' * 10)
    if o == 1:
        print(f'A Soma de {pn} e {sn} é \033[:32m{pn+sn}')
        print('\033[m-=-' * 10)
    elif o == 2:
        print(f'A Subtração de {pn} e {sn} é \033[:32m{pn-sn}')
        print('\033[m-=-' * 10)
    elif o == 3:
        print(f'A Multiplicação de {pn} e {sn} é \033[:32m{pn*sn}')
        print('\033[m-=-' * 10)
    elif o == 4:
        print(f'A Divisão de {pn} e {sn} é \033[:32m{pn/sn}')
        print('\033[m-=-' * 10)
    elif o == 5:
        while n != '.':
            n = int(input(f'De qual número deseja ({pn}/{sn})? '))
            if n == pn:
                print(f'A Raiz Quadrada de {n} é {sqrt(n)}')
                n = str('.')
                print('\033[m-=-' * 10)
            elif n == sn:
                print(f'A Raiz Quadrada de {n} é {sqrt(n)}')
                n = str('.')
                print('\033[m-=-' * 10)
            else:
                print('Número Inválido!')
                print('\033[m-=-' * 10)
        n = int(0)
    elif o == 6:
        print(f'A Potenciação de {pn}^{sn} é {pn**sn}')
        print ('\033[m-=-'*10)
print('Encerrando...')
sleep(1)