# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

c = float(input('Valor da casa: R$'))
s = float(input('Salário do comprador: R$'))
a = int(input('Quantos anos de financiamento? '))
p = c/(a*12)
s = s*0.30
print(f'Para pagar uma casa de R${c:.2f} em {a} anos a prestação será de RS{p:.2f}')

if p > s:
    print('Empréstimo NEGADO!')
elif p <= s:
    print('Empréstimo ACEITO!')
