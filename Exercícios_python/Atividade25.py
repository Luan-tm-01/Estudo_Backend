#Faça um programa que calcule a soma entre todos os números que são múltiplos de três e  impares que se encontram no intervalo
#de 1 até 500.

i2 = 0
i3 = 0
for i in range (1, 501):
    if i % 3 == 0 and i % 2 !=0:
        i3 += 1
        i2 += i
print(f'A soma de todos os {i3} valores solicitados é {i2}')
