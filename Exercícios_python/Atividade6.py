#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

n = str(input("Digite seu nome Completo: ")).strip().split()

t = len(n)
fn = n[0]
ln = n[t-1]

print(f'Seu Primeiro nome é {fn}')
print(f'Seu Último nome é {ln}')