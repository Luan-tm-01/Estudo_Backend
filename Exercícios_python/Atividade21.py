# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço formal
# 3x ou mais no cartão: 20% de juros

print('='*7,'LOJA','='*7)
c = float(input(f'Preço das compras: R$'))
print('FORMAS DE PAGAMENTO\n[ 1 ] à vista dinheiro/cheque\n[ 2 ] à vista cartão\n[ 3 ] 2x no cartão\n[ 4 ] 3x ou mais no cartão')
o = int(input('Qual é a opção? '))
if o == 1:
    print(f'Sua compra de R${c:.2f} vai custar R${c*0.9:.2f} no final.')
elif o == 2:
    print(f'Sua compra de R${c:.2f} vai custar R${c*0.95:.2f} no final.')
elif o == 3:
    print(f'Sua compra será parcelada em 2x de R${c/2:.2f} COM JUROS')
elif o == 4:
    p = int(input('Quantas parcelas? '))
    j = (c/p)
    print(f'Sua compra será parcelada em {p}x de R${j+(j*0.20):.2f} COM JUROS\nSua compra de R${c:.2f} vai custar R${c+(c*0.20):.2f}')