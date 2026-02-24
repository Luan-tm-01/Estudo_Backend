# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

s = float(input('Qual é o salário de funcionário? R$'))
if s <= 1250:
    print(f'Quem ganhava R${s:.2f} passa a ganhar R${s*1.15:.2f} agora.')
else:
    print(f'Quem ganhava R${s:.2f} passa a ganhar R${s*1.10:.2f} agora.')