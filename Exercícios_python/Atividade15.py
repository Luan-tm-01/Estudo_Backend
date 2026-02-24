# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.

n = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão:\n[ 1 ] converter para BINÁRIO\n[ 2 ] converter para OCTAL\n[ 3 ] converter para HEXADECIMAL')
o = int(input('Sua opção: '))
if o == 1:
    print(f'{n} convertido para BINÁRIO é igual a {bin(n)[2:]}')
elif o == 2:
    print(f'{n} convertido para OCTAL é igual a {oct(n)[2:]}')
elif o == 3:
    print(f'{n} convertido para HEXADECIMAL é igual a {hex(n)[2:].upper()}')