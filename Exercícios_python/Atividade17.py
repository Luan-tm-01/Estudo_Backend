# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

an = int(input('Ano de nascimento: '))
aa = date.today().year
print(f'Quem nasceu em {an} tem {aa-an} em {aa}.')
if aa-an<18:
    print(f'Ainda faltam {18-(aa-an)} anos para o alistamento\nSeu alistamento será em {(18-(aa-an))+aa}')
elif aa-an == 18:
    print(f'Você tem que se alistar IMEDIATAMENTE!')
else:
    print(f'Você já deveria ter se alistado há {(aa-an)-18} anos.\nSeu alistamento foi em {aa-((aa-an)-18)}.')