# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# IMC abaixo de 18,5: Abaixo do Peso
# Entre 18,5 e 25: Peso Ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade Mórbida

p = int(input('Qual é seu peso(Kg)? '))
a = float(input('Qual é sua altura(m)? '))
imc = p/(a**2)
print(f'O IMC dessa pessoa é de {imc}')
if imc < 18.5:
    print()
elif imc >= 18.5 and imc < 25:
    print()
elif imc >= 25 and imc < 30:
    print()
elif imc >= 30 and imc < 40:
    print()
else:
    print()