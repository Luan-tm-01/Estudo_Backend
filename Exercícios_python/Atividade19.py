# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JÚNIOR
# Até 25 anos: SÊNIOR
# Acima de 25 anos: MASTER

from datetime import date

an = int(input('Ano de Nascimento: '))
aa = date.today().year
i = aa-an
print(f'O atleta tem {i} anos.')
if i <= 9:
    print('Classificação: MIRIM')
elif i <= 14:
    print('Classificação: INFANTIL')
elif i <= 19:
    print('Classificação: JÚNIOR')
elif i <= 25:
    print('Classificação: SENIOR')
else:
    print('Classificação: MASTER')
