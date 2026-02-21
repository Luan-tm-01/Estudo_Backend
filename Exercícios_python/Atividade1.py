# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas e minúsculas
# Quantas letras ao t0do (sem considerar espaços)
# Quantas letras tem o primeiro nome.

n = str(input('Digite seu Nome Completo: '))
print('Analisando seu Nome...')
print(f'Seu nome em Maiúsculo é {n.upper()}')
print(f'Seu nome em Minúsculo é {n.lower()}')
print(f'Seu nome tem ao todo {len(n) - n.count(' ')} letras')
n = n.split()
print(f'Seu primeiro nome é {n[0]} e ele tem {len(n[0])} letras')
