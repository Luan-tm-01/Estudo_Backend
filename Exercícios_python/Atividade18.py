# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO

pn = float(input('Primeira nota: '))
sn = float(input('Segunda nota: '))
m = (pn+sn)/2
print(f'Tirando {pn} e {sn}, a média do aluno é {m:.1f}')
if m < 5:
    print('O aluno está REPROVADO.')
elif m >= 5 and m <= 6.9:
    print('O aluno está em RECUPERAÇÃO.')
else:
    print('O aluno está APROVADO.')